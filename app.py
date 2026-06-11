import streamlit as st
from EDUSense_engine import analyze

st.set_page_config(page_title="EDUSense-AI", layout="centered")

# Header
st.title("🧠 EDUSense-AI")
st.caption("AI-Powered Student Misconception Diagnostic System (PSMDS)")
st.write("Created by Mr. Stewart")
st.write("Powered by curiosity, the desire to learn, and the need for coffee ☕")

st.markdown("---")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Enter: expression | answer | student thinking")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        expression, student_answer, student_work = prompt.split("|")

        results = analyze(expression.strip(), student_answer.strip(), student_work.strip())

        response = ""

        for r in results:
            response += f"🧠 **I noticed:** {r['misconception']}\n\n"
            response += f"💬 **Feedback:** {r['student_feedback']}\n\n"
            response += f"📘 **Teacher insight:** {r['teacher_note']}\n\n---\n\n"

    except:
        response = "⚠️ Use format: expression | answer | student work"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
