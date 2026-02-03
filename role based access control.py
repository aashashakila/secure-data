import streamlit as st
import pandas as pd

st.set_page_config(page_title="Secure Data Processing Platform", layout="centered")

# ---------------- USER DATABASE (Demo Purpose) ----------------
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
            st.rerun()
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
        st.rerun()

    st.title("📊 Dashboard")

    # -------- VIEW ACCESS (Admin, User, Viewer) --------
    st.subheader("🔍 View Data")
    sample_data = pd.DataFrame({
        "Employee": ["A", "B", "C"],
        "Department": ["IT", "HR", "Finance"],
        "Salary": [30000, 40000, 35000]
    })
    st.dataframe(sample_data)

    # -------- UPLOAD ACCESS (Admin, User) --------
    if st.session_state.role in ["Admin", "User"]:
        st.subheader("📤 Upload Data")
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully")
            st.dataframe(df)

    # -------- ADMIN ONLY ACCESS --------
    if st.session_state.role == "Admin":
        st.subheader("⚠️ Admin Controls")
        if st.button("Delete Data (Demo Action)"):
            st.success("Data deleted successfully (demo)")

        st.button("Delete Data")
