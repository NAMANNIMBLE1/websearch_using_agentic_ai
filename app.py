# tools 
from langchain_community.tools import ArxivQueryRun , WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper , WikipediaAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_agentql.tools import ExtractWebDataTool
# libraries for the chatbot langgraph 
from IPython.display import Image , display 
from langgraph.graph import StateGraph , START ,END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
# initializing the llm 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
# playwright install
import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.messages import HumanMessage
os.environ["TAVILY_API_KEY"]= os.getenv("TAVILY_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["AGENTQL_API_KEY"] = os.getenv("AGENTQL_API_KEY")


# tool1 
api_wrapper_arxiv = ArxivAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=5000
)
arxiv = ArxivQueryRun(
    api_wrapper=api_wrapper_arxiv,
    name="query arxiv papers"
)
#tool2 
wikipedia_api_wrapper = WikipediaAPIWrapper(
    top_k_results= 2,
    # lang="english",
    doc_content_chars_max=5000
)

wikipedia = WikipediaQueryRun(
    api_wrapper=wikipedia_api_wrapper,
    name="query wikipedia search"
)
# tool 3
# tavily search tool 
tavily = TavilySearchResults()
# tool4 
extract_web_data_tool = ExtractWebDataTool(
    mode = "fast",
    is_scroll_to_bottom_enabled = True,
)

# combing the tools 
tools = [arxiv , tavily , extract_web_data_tool] # removing wikipedia as it causes some errors 

llm = ChatGroq(
    model="Gemma2-9b-It"
)

# combining llm with tools
llm_with_tools = llm.bind_tools(tools=tools)

# workflow

# state schema
from langchain_core.messages import AnyMessage # human message or ai-message
from typing_extensions import TypedDict 
from typing import Annotated # labelling
from langgraph.graph import add_messages ## reducers in langgraph --> not overwrite in the state but append the messages

# designing state schema
class State(TypedDict):
    messages : Annotated[list[AnyMessage] , add_messages]
    

# node definition
def tool_calling_llm(state : State):
    # Invoke LLM with the messages from state and return as a list in messages key
    messages = llm_with_tools.invoke(state["messages"])
    return {"messages": [messages]}

# building graph 
builder = StateGraph(State)
builder.add_node("tool_calling_llm" , tool_calling_llm) # node  1 
builder.add_node("tools" , ToolNode(tools)) # node 2 

## EDGES 
builder.add_edge(START , "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    # if message(result) => tool call -> tool routes to tools 
    # if ! tool call -> tool condition routes to 
    tools_condition,
)
builder.add_edge("tools" , END)

graph = builder.compile()

# streamlit app

st.set_page_config(page_title="🔍 ChatGraph AI", page_icon="🧠")
st.title("🤖 Chat with Web")
st.markdown("Ask anything! The model will think, search, and respond intelligently.")

# Input box
user_input = st.text_input("💬 What would you like to ask?", "")

# Send button
if st.button("Send") and user_input.strip():
    with st.spinner("Thinking... 🧠"):
        try:
            # Pass message into LangGraph
            result = graph.invoke({
                "messages": [HumanMessage(content=user_input)]
            })

            # Extract and display the final AI message
            response_message = result["messages"][-1]
            st.success("📬 Chatbot Response:")
            st.markdown(response_message.content)

            # Optionally show all message history
            with st.expander("🗃️ Full Message History"):
                for msg in result["messages"]:
                    role = "🧑 You" if msg.type == "human" else "🤖 Bot"
                    st.markdown(f"**{role}:** {msg.content}")

        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")

with st.sidebar:
    st.header("🧠 Assistant Info")
    st.markdown("""
**Welcome!** This intelligent assistant can answer your questions using specialized tools:

### 🔍 Tools Available:

- **📄 ArXiv**  
  Searches for academic and research papers in domains like computer science, physics, AI, and mathematics. Ideal for technical and scholarly information.

- **🌐 Tavily**  
  Performs fast and up-to-date web searches. Useful for current events, news, or modern topics where ArXiv might not be relevant.

- **🧰 Extract Web Data**  
  Extracts structured data (tables, posts, prices, metrics, etc.) directly from any web page URL. Best for detailed or real-time content scraping.
  using query for example: \n  posts[]{ title url date author} and provide the url for extraction
  
---
💡 *This assistant never answers from its own memory. It always uses one of these tools to provide accurate and verifiable results.*
""")

st.markdown("---")
st.caption("Created by Naman Nimble | Powered by LangChain, Tavily, and ArXiv")
