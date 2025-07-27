import streamlit as st
st.set_page_config(page_title="AI Career Coach", page_icon="🧠")

import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from save_user import save_user

# --- Load configuration from YAML file ---
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# --- Initialize the Authenticator ---
authenticator = stauth.Authenticate(
    credentials=config["credentials"],
    cookie_name=config["cookie"]["name"],
    key=config["cookie"]["key"],
    cookie_expiry_days=config["cookie"]["expiry_days"]
)

# --- Display Login Form ---
authenticator.login(location="main")

# --- Check authentication status using session_state ---
auth_status = st.session_state.get("authentication_status", None)

if auth_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {st.session_state.get('name', 'User')} 👋")

    st.sidebar.title("🔗 Navigation")
    page = st.sidebar.radio("Go to", ["Career Advice", "Resume Builder", "Interview Coach"])

    if page == "Career Advice":
        from pages import career_advice
        career_advice.run()

    elif page == "Resume Builder":
        from pages import resume
        resume.run()

    elif page == "Interview Coach":
        from pages import interview_questions
        interview_questions.run()

elif auth_status is False:
    st.error("❌ Incorrect username or password.")

elif auth_status is None:
    st.warning("👋 Please enter your username and password.")

# --- Registration Section ---
with st.expander("🔐 New user? Register here"):
    new_name = st.text_input("Full Name")
    new_email = st.text_input("Email")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Register"):
        success, msg = save_user(new_username, new_name, new_email, new_password)
        if success:
            st.success("✅ " + msg)
        else:
            st.error("❌ " + msg)






