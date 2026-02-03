import streamlit as st
import pandas as pd

st.set_page_config(page_title="Secure Data Platform")

USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "user1": {"password": "user123", "role": "User"},
    "viewer1": {"password": "view123", "role": "Viewer"}
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = ""
    st.session_state.username = ""

# -------- LOGIN PAGE --------
if not st.session_state.logged_in:
    st.title("🔐 Secure Data Processing Platform")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = USERS[username]["role"]
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

# -------- DASHBOARD --------
else:
    st.sidebar.success(f"User: {st.session_state.username}")
    st.sidebar.info(f"Role: {st.session_state.role}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = ""
        st.session_state.username = ""

    st.title("📊 Dashboard")

    st.subheader("View Data")
    df = pd.DataFrame({
        "Name": ["A", "B", "C"],
        "Score": [85, 90, 78]
    })
    st.dataframe(df)

    if st.session_state.role in ["Admin", "User"]:
        st.subheader("Upload Data")
        file = st.file_uploader("Upload CSV", type=["csv"])
        if file:
            st.dataframe(pd.read_csv(file))

    if st.session_state.role == "Admin":
        st.subheader("Admin Control")
        st.button("Delete Data")
