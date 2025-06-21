import streamlit as st
from transformers import pipeline
import random

# Load LLaMA 3 (text generation pipeline)
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        token="your_huggingface_token_here"  # 👈 Add again here
    )

generator = load_model()

# Initialize state
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# Title
st.title("💡 AI Career Counselor")
st.subheader("Answer a few smart questions and let's explore your career path!")

# Step 0: User Input
if st.session_state.step == 0:
    name = st.text_input("👤 What's your name?")
    age = st.number_input("🎂 Your age", 10, 30, 17)
    interest = st.text_input("💭 What are your interests? (e.g., tech, creativity, business)")

    if st.button("Start Quiz"):
        st.session_state.name = name
        st.session_state.age = age
        st.session_state.interest = interest
        st.session_state.step = 1

# Step 1: Generate quiz questions using LLaMA 3
elif st.session_state.step == 1:
    prompt = (
        f"Create 5 short, fun multiple choice questions for a career interest quiz "
        f"for a {st.session_state.age}-year-old who is interested in {st.session_state.interest}. "
        "Each question should have 4 options labeled A, B, C, D."
    )

    result = generator(prompt, max_new_tokens=512)[0]["generated_text"]

    if "questions" not in st.session_state:
        questions = result.split('\n\n')[:5]  # crude way to split
        st.session_state.questions = questions

    st.write("### Question 1")
    st.write(st.session_state.questions[0])
    answer = st.radio("Choose your answer:", ["A", "B", "C", "D"])

    if st.button("Next"):
        st.session_state.answers.append(answer)
        st.session_state.step = 2

# Step 2: To be continued in Part 2...
