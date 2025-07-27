# pages/career_advice.py
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from prompts import generate_career_prompt
from ui_style import apply_custom_theme

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

def run():
    apply_custom_theme()
    st.title("🎯 Career Advice")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    name = st.text_input("👤 Full Name")
    degree = st.text_input("🎓 Degree")
    skills = st.text_area("🧠 Skills (Bullets Form)")
    interests = st.text_area("💡 Interests (Bullets Form)")
    personality = st.selectbox("🧬 Personality Type", ["Introvert", "Extrovert", "Ambivert"])
    goal = st.text_input("🎯 Career Goal (optional)")

    if st.button("🔍 Get Career Advice"):
        if not all([name, degree, skills, interests, personality]):
            st.warning("Please fill in all fields.")
        else:
            with st.spinner("Generating advice..."):
                try:
                    prompt = generate_career_prompt(name, degree, skills, interests, personality, goal)
                    response = client.chat.completions.create(
                        model="llama3-70b-8192",
                        messages=[
                            {"role": "system", "content": "You are a helpful career advisor."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7
                    )
                    st.subheader("🧠 Your AI-Powered Career Advice:")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Quick Access")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🏠 Home")
        st.button("🎤 Interview Coach")
    with col2:
        st.button("📄 Resume Builder")
        st.button("🛠️ Admin Panel")
    st.markdown('</div>', unsafe_allow_html=True)