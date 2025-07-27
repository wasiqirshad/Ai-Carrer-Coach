import streamlit as st
from ui_style import apply_custom_theme
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run():
    apply_custom_theme()

    st.title("🎤 Interview Coach")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🧪 Let AI prepare you for interviews")

    role = st.text_input("💼 Desired Role or Job Title")

    if st.button("🧠 Generate Interview Questions"):
        if not role:
            st.warning("Please enter a job title.")
        else:
            with st.spinner("Generating questions..."):
                try:
                    prompt = f"Generate 5 realistic interview questions for a {role} role."

                    response = client.chat.completions.create(
                        model="llama3-70b-8192",
                        messages=[
                            {"role": "system", "content": "You are an expert interview coach."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.6
                    )

                    st.success("✅ Here are your questions:")
                    st.markdown(response.choices[0].message.content)

                except Exception as e:
                    st.error(f"❌ Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

    # Dummy Buttons for navigation
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Quick Access")
    col1, col2 = st.columns(2)
    with col1:
        st.button("📄 Resume Builder")
        st.button("📈 Career Advice")
    with col2:
        st.button("🧠 Interview Coach")
        st.button("🛠️ Admin Panel")
    st.markdown('</div>', unsafe_allow_html=True)
