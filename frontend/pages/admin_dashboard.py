def run():
    import streamlit as st
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt

    BASE_URL = "http://127.0.0.1:8000"  # 🔥 change to deployed URL later

    # ==============================
    # 🎨 CLEAN UI (HIDE PAGES)
    # ==============================
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display:none;}
    </style>
    """, unsafe_allow_html=True)

    # ==============================
    # 🔐 SESSION CHECK
    # ==============================
    if not st.session_state.get("logged_in"):
        st.warning("Please login first")
        st.stop()

    if st.session_state.role != "admin":
        st.error("Unauthorized access")
        st.stop()

    # ==============================
    # 🏷️ HEADER
    # ==============================
    st.title("📊 Admin Dashboard")
    st.success(f"Welcome Admin {st.session_state.username} 👑")

    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.rerun()

    st.markdown("---")

    # ==============================
    # 📊 KPI METRICS
    # ==============================
    col1, col2, col3 = st.columns(3)

    res_users = requests.get(f"{BASE_URL}/admin/total-users")
    total_users = res_users.json().get("total_users", 0) if res_users.status_code == 200 else 0

    res_active = requests.get(f"{BASE_URL}/admin/active-users")
    active_data = res_active.json() if res_active.status_code == 200 else []
    active_users = len(active_data)

    res_feedback = requests.get(f"{BASE_URL}/admin/feedbacks")
    feedback_data = res_feedback.json() if res_feedback.status_code == 200 else []
    total_feedback = len(feedback_data)

    col1.metric("👥 Total Users", total_users)
    col2.metric("🟢 Active Users", active_users)
    col3.metric("💬 Feedbacks", total_feedback)

    st.markdown("---")

    # ==============================
    # 📊 MODULE USAGE (FIXED UI)
    # ==============================
    st.subheader("📊 Module Usage Analytics")

    res_usage = requests.get(f"{BASE_URL}/admin/module-usage")

    if res_usage.status_code == 200:
        data = res_usage.json()

        if data:
            df = pd.DataFrame(data)

            # 🔥 SIDE-BY-SIDE LAYOUT
            col1, col2 = st.columns(2)

            # -------- BAR CHART --------
            with col1:
                st.markdown("### 📊 Usage Count")

                fig1, ax1 = plt.subplots(figsize=(5, 3))
                ax1.bar(df["module"], df["count"])
                ax1.set_xlabel("Modules")
                ax1.set_ylabel("Usage")
                ax1.set_title("Module Usage")

                plt.tight_layout()
                st.pyplot(fig1)

            # -------- PIE CHART --------
            with col2:
                st.markdown("### 🥧 Distribution")

                fig2, ax2 = plt.subplots(figsize=(4, 4))
                ax2.pie(df["count"], labels=df["module"], autopct="%1.1f%%")
                ax2.set_title("Usage Share")

                plt.tight_layout()
                st.pyplot(fig2)

        else:
            st.info("No module usage data available")

    st.markdown("---")

    # ==============================
    # 📈 ACTIVE USERS TABLE
    # ==============================
    st.subheader("📈 Active Users")

    if active_data:
        df_active = pd.DataFrame(active_data)
        st.dataframe(df_active, use_container_width=True)
    else:
        st.info("No active users data")

    # ==============================
    # 💬 FEEDBACK TABLE
    # ==============================
    st.subheader("💬 User Feedback")

    if feedback_data:
        df_feedback = pd.DataFrame(feedback_data)
        st.dataframe(df_feedback, use_container_width=True)
    else:
        st.info("No feedback available")