import streamlit as st
import os
from huggingface_hub import InferenceClient

# Load your Hugging Face token from Streamlit secrets
HF_TOKEN = st.secrets["hf_token"]

# Initialize the Hugging Face Inference Client
client = InferenceClient(
    provider="nscale",
    api_key=HF_TOKEN,
)

st.set_page_config(page_title="LLaMA 3.1 Chat 💬", layout="centered")
st.title("🤖 Chat with LLaMA 3.1 (8B-Instruct)")

# User input prompt
user_input = st.text_area("🗣️ Ask something:", value="What is the capital of France?", height=100)

if st.button("✨ Get Answer"):
    with st.spinner("Thinking with LLaMA 3.1..."):
        try:
            response = client.chat.completions.create(
                model="meta-llama/Llama-3.1-8B-Instruct",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            st.markdown("### 🧠 Response:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
