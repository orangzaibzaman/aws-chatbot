import streamlit as st 
import chatbot_backend as backend

#1 Set Title for Chatbot 
# https://docs.streamlit.io/library/api-reference/text/st.title
st.title("Hi, This is Custom chatbot :sunglasses:")

#2 Set LangChain memory to the session cache - initialize memory
# Session State - https://docs.streamlit.io/library/api-reference/session-state
if 'memory' not in st.session_state: 
    st.session_state.memory = backend.chatbot_memory()  

#3 Add the UI chat history to the session cache - initialize chat history
# Session State - https://docs.streamlit.io/library/api-reference/session-state
if 'chat_history' not in st.session_state: 
    st.session_state.chat_history = [] 

#4 Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
# with = try/catch
for message in st.session_state.chat_history: 
    with st.chat_message(message["role"]): 
        st.markdown(message["text"]) 

#5 Enter chatbot input box    
input_text = st.chat_input("Hi! This is a custom chatbot, how can I help ?")

if input_text: 
    with st.chat_message("user"): 
        st.markdown(input_text) 
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) 

#6 Call the model
    chat_response = backend.chatbot_conversation(input_prompt=input_text, memory=st.session_state.memory)
     
    with st.chat_message("assistant"): 
        st.markdown(chat_response) 
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) 
