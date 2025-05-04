
# Agentic AI for web search using Gemma3 and Langgraph 

## Overview

This porject focus on implementing a langgraph architecture to connect 
open source LLM to the diferent agents available for searching and loading data based on the context porvided by the use and similarity score of the search making a web search bot retrieving latest news , trends and information accross the internet from diffrent resources.




![logo](https://ai-pro.org/wp-content/uploads/2025/02/Google-Gemma-a-small-language-model-from-Google.jpg)


## Screenshots


![Alt Text](https://github.com/NAMANNIMBLE1/websearch_using_agentic_ai/images
/archietectureg)

![Alt Text](https://github.com/NAMANNIMBLE1/websearch_using_agentic_ai/images
/demo)


## API Reference

#### Get item

```http
  https://python.langchain.com/docs/introduction/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `LANGCHAIN_API_KEY` | `string` | **Required**. Your API key |

#### Get item

```http
  https://console.groq.com/keys
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `GROQ_API_KEY`      | `string` | **Required**. Your API key |

#### Get item

```http
  https://app.tavily.com/home
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `TAVILY_API_KEY`      | `string` | **Required**. Your API key |

#### Get item

```http
  https://www.agentql.com/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `AGENTQL_API_KEY`      | `string` | **Required**. Your API key |

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GROQ_API_KEY`
`TAVILY_API_KEY`
`AGENTQL_API_KEY`
`LANGCHAIN_API_KEY`


## Installation

Installation
To run this project, you need the following Python libraries:

```bash
    pip install uv
    uv pip install pydantic
    uv pip install langchain
    uv pip install langgraph
    uv pip install langchain-core 
    uv pip install langchain-community 
    uv pip install python-dotenv 
    uv pip install langchain-groq
    uv pip install arxiv
    uv pip install wikipedia
    uv pip install pymupdf 
    uv pip install langchain-agentql
    uv pip install streamlit
    uv pip install asyncio
    uv pip install IPython
    uv pip install nest_asyncio
```

for running the app.py file 
``` bash 
    streamlit run app.py 
```




## Run Locally

Clone the project

```bash
  git clone https://github.com/NAMANNIMBLE1/websearch_using_agentic_ai
```

Start the server

```bash
  streamlit run app.py
```


## Documentation

[Langchain Documentation](https://python.langchain.com/docs/introduction/n)

[Langgraph Documentation](https://langchain-ai.github.io/langgraph/tutorials/introduction/S)
## Authors

- [@NAMANNIMBLE1](https://github.com/NAMANNIMBLE1)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

