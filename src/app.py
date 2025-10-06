import streamlit as st
from llm_interface import LLMWrapper

# Set page config
st.set_page_config(
    page_title="GST FAQ Chatbot",
    page_icon="💬",
    layout="centered"
)

def main():
    st.title("GST FAQ Chatbot")
    st.write("Ask me anything about GST!")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize LLM
    if "llm" not in st.session_state:
        st.session_state.llm = LLMWrapper()
    
    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if prompt := st.chat_input("Ask me about GST..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            response = st.session_state.llm.generate_response(prompt)
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
