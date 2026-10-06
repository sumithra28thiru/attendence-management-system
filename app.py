import streamlit as st
import pandas as pd
from database import login, get_attendance, update_attendance


st.set_page_config(
    page_title="Attendance Portal",
    page_icon="📚"
)


# ---------------- LOGIN ----------------

def login_page():

    st.title("📚 Attendance Portal")
    st.write("Student Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login(username, password)

        if user:
            st.session_state.logged_in = True
            st.session_state.student_id = user[0]
            st.session_state.student_name = user[1]

            st.rerun()

        else:
            st.error("Invalid username or password")


# ---------------- DASHBOARD ----------------

def dashboard():

    st.title("📊 Attendance Dashboard")

    st.write(
        f"Welcome, **{st.session_state.student_name}**"
    )

    data = get_attendance(
        st.session_state.student_id
    )

    df = pd.DataFrame(
        data,
        columns=[
            "Date",
            "Subject",
            "Status"
        ]
    )

    # Attendance calculation
    total = len(df)

    present = len(
        df[df["Status"] == "Present"]
    )

    absent = len(
        df[df["Status"] == "Absent"]
    )

    percentage = 0

    if total > 0:
        percentage = round(
            (present / total) * 100,
            2
        )

    # Statistics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Attendance",
        f"{percentage}%"
    )

    col2.metric(
        "Present",
        present
    )

    col3.metric(
        "Absent",
        absent
    )

    st.divider()

    st.subheader("Attendance Records")

    st.dataframe(
        df,
        use_container_width=True
    )

    # ---------------- UPDATE ATTENDANCE ----------------

    st.subheader("Update Attendance")

    selected_date = st.selectbox(
        "Select Date",
        df["Date"]
    )

    selected_status = st.selectbox(
        "Select Status",
        ["Present", "Absent"]
    )

    if st.button("Update"):

        update_attendance(
            st.session_state.student_id,
            selected_date,
            selected_status
        )

        st.success("Attendance updated!")

        st.rerun()

    # Logout
    st.divider()

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.student_id = None
        st.session_state.student_name = None

        st.rerun()


# ---------------- MAIN ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if st.session_state.logged_in:
    dashboard()
else:
    login_page()