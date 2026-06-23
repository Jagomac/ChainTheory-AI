import streamlit as st
from ChainTheory_AI import analyze

# -----------------------------------
# HEADER
# -----------------------------------
st.title("ChainTheory-AI")
st.subheader("Diagnosing how students think, one step at a time")
st.caption("Built by James Stewart")

st.markdown("---")

# -----------------------------------
# INPUT SECTION
# -----------------------------------
st.write("### Student Input")

math_expression = st.text_input("Math Expression:")

student_answer = st.text_input("Student Answer:")

student_explanation = st.text_area("Student Explanation:")

# -----------------------------------
# ANALYZE BUTTON
# -----------------------------------
if st.button("Analyze Student Thinking"):
    if math_expression and student_answer and student_explanation:
        
        # You can later upgrade this logic
        result = analyze(math_expression)

        st.markdown("### Analysis Result")
        st.success(result)

    else:
        st.warning("Please fill in all fields.")
