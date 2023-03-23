import streamlit as st 
import openai

st.write("its my first App")

def show_message(text):
  messages_str = [
      f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][1:]
  ]
  text.text_area("messages", value = str("\n\n".join(messages_str)), height=400 )
  
  
BASE_PROMPT = [{"role":"system", "content":"your assistant."}]

st.subheader("ChatGpt from Chaschen")

text = st.empty()
show_message(text)
