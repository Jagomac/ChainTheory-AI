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

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# -----------------------------------
# HEADER
# -----------------------------------
st.title("🧠 ChainTheory-AI 🧠")
st.subheader("Understanding how students think — not just what they answer")
st.caption("Built by Mr. Stewart")
st.markdown("Powered by curiosity, a drive to learn, and a lot of coffee ☕")

st.markdown("---")

# -----------------------------------
# TOP CONTROL BAR (MODE + PASSWORD)
# -----------------------------------
col1, col2 = st.columns([2, 1])

with col2:
    password_input = st.text_input("🔐 Teacher", type="password")
    if password_input == "root":
        st.session_state.authenticated = True

with col1:
    if st.session_state.authenticated:
        mode = st.radio("Mode", ["Student", "Teacher Dashboard"])
    else:
        mode = "Student"

st.markdown("---")

# ===================================
# STUDENT MODE
# ===================================
if mode == "Student":

    st.markdown("## ✏️ Student Input")

    math_expression = st.text_input("Math Expression:")
    student_answer = st.text_input("Student Answer:")
    student_explanation = st.text_area("Student Explanation:")

    if st.button("Analyze Student Thinking"):

        if math_expression and student_answer and student_explanation:

            # ✅ Nonsense filter
            nonsense_words = ["idk", "lol", "random", "???", "asdf", "bruh"]

            if any(word in student_explanation.lower() for word in nonsense_words):
                st.warning("⚠️ Try explaining your thinking more clearly.")
                st.stop()

            try:
                result = analyze(
                    math_expression,
                    student_answer,
                    student_explanation
                )

                st.success("✅ Analysis complete")

                # ✅ Save to dashboard data
                st.session_state.class_data.append(result)

                # ✅ Output
                if isinstance(result, list):
                    for issue in result:
                        st.markdown("### ⚠️ Misconception")
                        st.write(f"**Issue:** {issue.get('misconception', '')}")
                        st.write(f"**Student Feedback:** {issue.get('student_feedback', '')}")
                        st.write(f"**Teacher Note:** {issue.get('teacher_note', '')}")
                        st.markdown("---")
                else:
                    st.markdown(result)

            except Exception:
                st.error("⚠️ Something went wrong. Try valid inputs.")

        else:
            st.warning("Please fill in all fields.")


# ===================================
# TEACHER DASHBOARD
# ===================================
if mode == "Teacher Dashboard":

    st.markdown("## 🧑‍🏫 Class Insight Dashboard")

    data = st.session_state.class_data

    if len(data) == 0:
        st.info("No data yet. Run student analyses first.")

    else:
        st.write(f"Total Attempts: {len(data)}")

        misconception_counts = {}

        for entry in data:
            if isinstance(entry, list):
                for issue in entry:
                    m = issue.get("misconception", "Unknown")
                    misconception_counts[m] = misconception_counts.get(m, 0) + 1

        st.markdown("### 📊 Common Misconceptions")

        # ✅ ONLY VALID LOOP
        for key, value in misconception_counts.items():
            st.write(f"- {key} → {value}")

        if len(misconception_counts) > 0:
            most_common = max(misconception_counts, key=misconception_counts.get)

            st.markdown("### 🧠 Insight")
            st.write(f"Most common issue: **{most_common}**")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Reset Data"):
            st.session_state.class_data = []
            st.success("Class data cleared")

    with col2:
        if st.button("Log Out"):
            st.session_state.authenticated = False
            st.success("Logged out")




# ---------------------------
# MISCONCEPTION COUNTS
# ---------------------------
        misconception_counts > 0

        for entry in data:

