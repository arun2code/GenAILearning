import streamlit as st
from langchain_community.llms import Ollama

st.title("Chat with me")

# Initialize session state for chat history if it doesn't exist
def init_session():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

init_session()

# Initialize the Ollama model
llm = Ollama(model="llama2", base_url='http://localhost:11434');

#llm = Ollama(model="llama2")

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user
user_input = st.chat_input("Say something...")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send message to Ollama model and get response
    response = llm.invoke(user_input)
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state["messages"].append({"role": "assistant", "content": response})
