import streamlit as st

st.set_page_config(page_title="Logix.ai Web", layout="wide")

# Styling
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #007bff; width: 100%; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("Logix.ai - Web Interface")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can Logix help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = f"Logix Analysis: Researching '{prompt}'..."
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
