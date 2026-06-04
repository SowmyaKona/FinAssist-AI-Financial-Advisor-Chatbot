import streamlit as st
from gemini_service import get_response

st.set_page_config(
    page_title="FinAssist AI",
    page_icon="💰"
)

st.title("💰 FinAssist AI")

st.warning(
    "⚠️ This chatbot provides educational financial information only and is not a substitute for professional financial advice."
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input(
    "Ask a financial question..."
)

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Analyzing your financial query..."):

        # Send only recent messages for token optimization
        recent_history = st.session_state.messages[-10:]

        # IMPORTANT FIX
        response = get_response(recent_history)

    with st.chat_message("assistant"):
        st.markdown(response)

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# Sidebar
with st.sidebar:

    st.title("💰 FinAssist AI")

    st.markdown("""
    ### Features

    ✅ Budget Planning

    ✅ Savings Strategies

    ✅ Investment Education

    ✅ Tax Basics

    ✅ Financial Planning

    ✅ Multi-turn Conversations
    """)

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()