import streamlit as st
import pandas as pd

st.set_page_config(page_title="Secure Data Platform", layout="centered")

# ---------------- USER DATABASE (Demo) ----------------
USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "user1": {"password": "user123", "role": "User"},
    "viewer1": {"password": "view123", "role": "Viewer"}
}

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:
    st.title("🔐 Secure Data Processing Platform")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = USERS[username]["role"]
            st.success(f"Login successful as {st.session_state.role}")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# ---------------- DASHBOARD ----------------
else:
    st.sidebar.success(f"User: {st.session_state.username}")
    st.sidebar.info(f"Role: {st.session_state.role}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.experimental_rerun()

    st.title("📊 Dashboard")

    # ---------------- VIEW ACCESS (ALL ROLES) ----------------
    st.subheader("🔍 View Data")
    df = pd.DataFrame({
        "Employee": ["A", "B", "C"],
        "Salary": [30000, 40000, 35000]
    })
    st.dataframe(df)

    # ---------------- USER + ADMIN ----------------
    if st.session_state.role in ["Admin", "User"]:
        st.subheader("📤 Upload Data")
        file = st.file_uploader("Upload CSV File", type=["csv"])
        if file:
            df = pd.read_csv(file)
            st.success("File uploaded successfully")
            st.dataframe(df)

    # ---------------- ADMIN ONLY ----------------
    if st.session_state.role == "Admin":
        st.subheader("⚠️ Admin Controls")
        if st.button("Delete Data (Demo Action)"):
            st.success("Data deleted successfully (demo)")
