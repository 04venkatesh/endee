""" import streamlit as st
import requests

st.title("📄 RAG Chatbot (Endee + Ollama + Mistral)")

if st.button("Process PDF"):
    res = requests.post("http://localhost:8000/process")
    st.success(res.json()["message"])

query = st.text_input("Ask a question from PDF")

if st.button("Ask"):
    res = requests.get("http://localhost:8000/ask", params={"query": query})
    st.write(res.json()["answer"]) """


import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("🤖 RAG Chatbot (Upload PDF + Chat)")

# -------------------------------
# 📤 Upload PDF
# -------------------------------
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    if st.button("Process PDF"):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post("http://localhost:8000/upload", files={"file": uploaded_file})

        if res.status_code == 200:
            st.success("PDF processed successfully!")
        else:
            st.error("Error processing PDF")


# -------------------------------
# 💬 Chat UI
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask something about your document..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from backend
    try:
        res = requests.get("http://localhost:8000/ask", params={"query": prompt})
        answer = res.json().get("answer", "No response")

    except Exception as e:
        answer = f"Error: {e}"

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)