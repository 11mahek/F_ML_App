import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="AI Career Quiz", layout="centered")

st.title("🎯 AI Career Quiz Generator")
st.markdown("Answer a few questions and let AI guide your career journey!")

# User Inputs
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=10, max_value=30, value=17)
interest = st.text_input("💭 Your Interests (e.g., tech, art, science)")

# Only proceed if all inputs are filled
if name and age and interest and st.button("✨ Generate Quiz"):
    with st.spinner("Generating smart quiz..."):
        # Hugging Face API Setup
        api_url = "https://api-inference.huggingface.co/models/google/flan-t5-base"
        headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
        prompt = (
            f"Create one fun multiple choice career quiz question for a {age}-year-old "
            f"interested in {interest}. Format it like:\n"
            f"Q: ...?\nA. ...\nB. ...\nC. ...\nD. ..."
        )

        # Send request to model
        response = requests.post(api_url, headers=headers, json={"inputs": prompt})
        
        # Handle response
        if response.status_code == 200:
            try:
                result = response.json()
                quiz = result[0]["generated_text"]
                st.markdown("### 📘 AI-Generated Quiz Question")
                st.markdown(f"{quiz}")
            except Exception as e:
                st.error("❌ Couldn't parse the AI response.")
        else:
            st.error(f"❌ API Error: {response.status_code}")
