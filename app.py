import streamlit as st
from ChainTheory_AI import analyze

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="ChainTheory-AI",
    layout="centered"
)

# -----------------------------------
# SESSION STORAGE
# -----------------------------------
if "class_data" not in st.session_state:
    st.session_state.class_data = []

# -----------------------------------
# HEADER
# -----------------------------------
st.title("🧠 ChainTheory-AI 🧠")
st.subheader("Understanding how students think — not just what they answer")
st.caption("Built by Mr. Stewart")
st.markdown("Powered by curiosity, a drive to learn, and a lot of coffee ☕")

st.markdown("---")

# -----------------------------------
# MODE SWITCH
# -----------------------------------
mode = st.radio("Select Mode", ["Student", "Teacher Dashboard"])

# ===================================
# STUDENT MODE
# ===================================
if mode == "Student":

    st.markdown("## ✏️ Student Input")

    math_expression = st.text_input("Math Expression:")
    student_answer = st.text_input("Student Answer:")
    student_explanation = st.text_area("Student Explanation:")


