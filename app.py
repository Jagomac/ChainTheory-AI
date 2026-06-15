
import streamlit as st
from EDUSense_engine import analyze

st.set_page_config(page_title="EDUSense‑AI", layout="centered")

st.title("EDUSense‑AI")
st.subheader("Math Misconception Diagnostic System")
st.caption("Powered by curiosity, the desire to learn, and the need for coffee ☕")


expression = st.text_input(
    "Math Expression",
    value="10 - 2 × 4"
)

student_answer = st.text_input(
    "Student Answer",
    value="32"
)

student_work = st.text_area(
    "Student Explanation",
    value="I did 10 minus 2 first, then multiplied."
)

if st.button("Analyze Student Thinking"):
    results = analyze(expression, student_answer, student_work)

    st.subheader("AI Analysis Output")

    for i, r in enumerate(results, 1):
        st.markdown(f"### Issue {i}")
        st.json(r)
