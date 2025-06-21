import streamlit as st
from transformers import pipeline

# Page setup
st.set_page_config(page_title="AI Career Quiz", layout="centered")
st.title("🎯 AI Career Quiz Generator")
st.markdown("Tell me your interest, and I’ll generate a fun career quiz question!")

# Load GPT-2 model (distil version for speed)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

# User input
interest = st.text_input("💭 What are your interests? (e.g., art, science, business)")

if st.button("Generate Question") and interest:
    with st.spinner("Generating your quiz question..."):
        prompt = (
            f"Create a fun multiple choice question for a career quiz. "
            f"The user is interested in {interest}. Use options A, B, C, D."
        )
        result = generator(prompt, max_new_tokens=60, do_sample=True, temperature=0.7)
        question = result[0]['generated_text']
        st.markdown("### ✨ Here's your AI-generated question:")
        st.markdown(f"```\n{question}\n```")
