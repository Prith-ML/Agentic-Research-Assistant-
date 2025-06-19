import streamlit as st 
from agent_runner import chat

st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("AI Research Assistant")

query = st.text_input("Ask a question about AI, ML, or Research Papers:")

if query:
    with st.spinner("Thinking..."):
        response = chat(query)

    st.markdown("### Answer")
    st.write(response)
