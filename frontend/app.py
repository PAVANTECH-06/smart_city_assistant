import streamlit as st
import requests

# ✅ MUST BE FIRST
st.set_page_config(page_title="Smart City Login", layout="wide")
st.markdown("""
<style>
/* Hide pages (app, user_dashboard, admin_dashboard) */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Optional: clean spacing */
section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

API_URL = "http://localhost:8000"

# -----------------------------
# SESSION STATE
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = None

if "selected_role" not in st.session_state:
    st.session_state.selected_role = None

# -----------------------------
# PAGE ROUTING (IMPORTANT)
# -----------------------------
if st.session_state.page == "user_dashboard":
    from pages import user_dashboard
    user_dashboard.run()
    st.stop()

elif st.session_state.page == "admin_dashboard":
    from pages import admin_dashboard
    admin_dashboard.run()
    st.stop()

# -----------------------------
# SIMPLE CSS (SAFE)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #f4f6f9;
}
h1, h2, h3 {
    color: #1f4e79;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LAYOUT
# -----------------------------
col1, col2 = st.columns([1, 1], gap="large")

# =============================
# LEFT PANEL
# =============================
with col1:
    st.title("🏙️ Smart City Assistant")

    st.write("Empowering cities with AI-driven insights for smarter, greener, and sustainable living.")

    st.markdown("### ✨ Features")
    st.write("📊 Real-time Analytics")
    st.write("🌍 Sustainability Insights")
    st.write("⚡ Smart Monitoring")
    st.write("🤖 AI Assistant")

    st.write("")
    st.caption("Built for Smart Governance & Future Cities 🚀")

# =============================
# RIGHT PANEL (LOGIN)
# =============================
with col2:

    st.title("🔐 Login")

    # ROLE BUTTONS
    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        if st.button("👤 User"):
            st.session_state.selected_role = "User"

    with col_btn2:
        if st.button("👑 Admin"):
            st.session_state.selected_role = "Admin"

    role = st.session_state.selected_role

    # BACK BUTTON
    if role:
        if st.button("⬅ Back"):
            st.session_state.selected_role = None
            st.rerun()

    # =============================
    # USER LOGIN
    # =============================
    if role == "User":

        tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

        # -------- LOGIN --------
        with tab1:
            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")

            if st.button("Login"):
                res = requests.post(f"{API_URL}/auth/login", json={
                    "username": username,
                    "password": password
                })

                if res.status_code == 200:
                    data = res.json()

                    st.session_state.logged_in = True
                    st.session_state.role = data["role"]
                    st.session_state.user_id = data["user_id"]
                    st.session_state.username = data["username"]

                    st.success(f"Welcome {data['username']} 👋")

                    st.session_state.page = "user_dashboard"
                    st.rerun()

                else:
                    st.error(f"Login failed: {res.text}")

        # -------- SIGNUP --------
        with tab2:
            new_user = st.text_input("New Username", key="signup_user")
            new_pass = st.text_input("New Password", type="password", key="signup_pass")

            if st.button("Create Account"):
                res = requests.post(f"{API_URL}/auth/signup", json={
                    "username": new_user,
                    "password": new_pass
                })

                if res.status_code == 200:
                    st.success("Account created 🎉")
                else:
                    st.error("User already exists")

    # =============================
    # ADMIN LOGIN
    # =============================
    elif role == "Admin":

        username = st.text_input("Admin Username", key="admin_user")
        password = st.text_input("Admin Password", type="password", key="admin_pass")

        if st.button("Login as Admin"):
            res = requests.post(f"{API_URL}/auth/login", json={
                "username": username,
                "password": password
            })

            if res.status_code == 200:
                data = res.json()

                st.session_state.logged_in = True
                st.session_state.role = data["role"]
                st.session_state.username = data["username"]

                st.success(f"Welcome Admin {data['username']} 👑")

                st.session_state.page = "admin_dashboard"
                st.rerun()

            else:
                st.error(f"Login failed: {res.text}")