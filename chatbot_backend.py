#1 import Langchain Modules

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_aws import ChatBedrockConverse

#2 Write a function for invoking model- client connection with Bedrock with profile, model_id & Inference params- model_kwargs
def chatbot():
    llm = ChatBedrockConverse(
        credentials_profile_name = 'default',
        model = "amazon.nova-pro-v1:0",
        temperature = 0.1,
        max_tokens = 1000)
    return llm

#3 Create a Function for ConversationBufferMemory (llm and max token limit)
def chatbot_memory():
    llm_data = chatbot()
    memory = ConversationSummaryBufferMemory(llm=llm_data, max_token_limit=2000)
    return memory

#4 Create a Function for Conversation Chain - Input text + Memory
def chatbot_conversation(input_prompt, memory):
    llm_chain_data = chatbot()
    llm_conversation = ConversationChain(
    llm = llm_chain_data, 
    memory = memory,
    verbose = True
)
#5 Chat response using invoke
    chatbot_reply = llm_conversation.invoke(input_prompt)
    return chatbot_reply['response']

