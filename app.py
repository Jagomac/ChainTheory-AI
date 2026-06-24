import streamlit as st
from ChainTheory_AI import analyze 

st.set_page_config(
    page_title="ChainTheory-AI",
    layout="centered"
)

# -----------------------------------
# PAGE SETUP
# -----------------------------------
st.set_page_config(
    page_title="ChainTheory-AI",
    layout="centered"
)

# -----------------------------------
# HEADER
# -----------------------------------
st.title("ChainTheory-AI")
st.subheader("Anayzing student's thinking, Revealing the why behind the answer, one step at a time.")
st.caption("Built by Mr.Stewart")
st.markdown("Powered by by Curiosity, the desire to learn, and the need for coffee ☕")


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

        # ✅ NONSENSE FILTER
        nonsense_words = ["idk", "lol", "random", "???", "asdf", "bruh"]

        if any(word in student_explanation.lower() for word in nonsense_words):
            st.warning("⚠️ Try explaining your thinking more clearly so the AI can help you.")
            st.stop()

        # ✅ SAFE ANALYZE BLOCK
        try:
            result = analyze(
                math_expression,
                student_answer,
                student_explanation
            )

            # ✅ OUTPUT DISPLAY
            if isinstance(result, list):
                for issue in result:
                    st.markdown("### ⚠️ Misconception Detected")
                    st.write(f"**Issue:** {issue.get('misconception', '')}")
                    st.write(f"**Student Feedback:** {issue.get('student_feedback', '')}")
                    st.write(f"**Teacher Note:** {issue.get('teacher_note', '')}")
                    st.markdown("---")
            else:
                st.markdown(result)

        except Exception:
            st.error("⚠️ Something went wrong. Try entering a valid math expression and explanation.")

    else:
        st.warning("Please fill in all fields.")




