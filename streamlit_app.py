import streamlit as st
import requests

# Title and subtitle
st.title("🦙 LLaMA 3 Chat")
st.subheader("Ask anything and let LLaMA 3 respond intelligently!")

# Prompt input
prompt = st.text_area("📝 Enter your prompt:", "Suggest 3 careers for someone who enjoys math and creativity.")

# Function to call Hugging Face Inference API
def query_llama(prompt):
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
    headers = {
        "Authorization": f"Bearer {st.secrets['HUGGINGFACE_TOKEN']}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Button to send prompt
if st.button("🚀 Generate Response"):
    with st.spinner("Calling LLaMA... please wait..."):
        output = query_llama(prompt)

        # Handle the response
        try:
            result = output[0]["generated_text"]
            st.success(result)
        except Exception as e:
            st.error("❌ Something went wrong.")
            st.error(output)
