# aws-chatbot
AWS Chatbot with DeepSeek, Langchain &amp; Streamlit

## Architecture

![image.png](attachment:879f8f42-dea5-415e-b5d4-4754cbda2de7:image.png)

## Prerequisites

- Python 3.12.4
- AWS CLI (Access Key + Secret key)
- AWS ToolKit and Boto3 extensions
- Configure IAM role  (Create a new role with attached policy)
- Anaconda Navigator
- Dependencies (pip install)
    - boto3==1.37.11
    - langchain==0.3.0
    - langchain-aws
    - streamlit==1.43.1
    - transformers
    - PyYAML

## Tech Stack & Libraries

Bedrock Converse API: Standardisation to use any models

Streamlit: Python library to build Front-end custom web apps for ML & Data Science 

LangChain: predict + run

- LangChain Prompt
- LangChain memory - ConversionBufferMemory
- ConversionChain (Connect prompt store, Bedrock and buffer memory)

Bedrock + DeepSeek: For back-end as FM

## Run

streamlit run chatbot_frontend.py

## Demo

## Bedrock monitoring using CloudWatch
