import streamlit as st

def apply_custom_theme():
    st.markdown("""
    <style>
    /* ===== Overall Page Background with Gradient ===== */
    .stApp {
        background: linear-gradient(135deg, #e0f2fe, #f8fafc);
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
    }

    /* ===== App Titles ===== */
    h1, h2, h3 {
        color: #0f172a;
        text-shadow: 1px 1px 1px rgba(0,0,0,0.05);
    }

    /* ===== Section Cards (Glassmorphism look) ===== */
    .card {
        background: rgba(255, 255, 255, 0.75);
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }

    /* ===== Buttons Styling ===== */
    div.stButton > button {
        background-color: #2563eb;
        color: white;
        padding: 0.6rem 1.2rem;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transition: all 0.3s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
        box-shadow: 0 6px 14px rgba(30, 64, 175, 0.35);
        transform: scale(1.03);
    }

    /* ===== Streamlit Input Fields ===== */
    input, textarea {
        border-radius: 10px !important;
        padding: 10px !important;
        border: 1px solid #d1d5db !important;
        background-color: #f9fafb !important;
    }

    /* ===== Radio Buttons / Selects ===== */
    div[data-baseweb="radio"], div[data-baseweb="select"] {
        background-color: #f1f5f9;
        padding: 10px;
        border-radius: 10px;
    }

    /* ===== Footer or Tag Line ===== */
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 3rem;
        font-size: 14px;
    }

    </style>
    """, unsafe_allow_html=True)

    # Optional Tag Line
    st.markdown('<div class="footer"> AI CAREER COACH | RESUME BUILDER | INTERVIEW TUTOR </div>', unsafe_allow_html=True)
    st.markdown('<div class="footer"> ✨ Developed By: INNOWAF TECH  ✨ </div>', unsafe_allow_html=True)
