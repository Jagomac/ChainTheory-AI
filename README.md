# EDUSense-AI 

EduSense AI is an education-focused AI system designed to help teachers:
- Plan standards-aligned lessons
- Differentiate instruction
- Detect student misconceptions
- Generate worksheets, rubrics, and feedback
- This AI also  was designed for students to help them understand the common errors in math


The system prioritizes explainability, alignment to Regents/NGSS standards,
and teacher-in-the-loop control.
## Phase 1 MVP

Goal:
Analyze student written responses and generate targeted, standards-aligned feedback.

Inputs:
- Lesson topic
- Relevant standard(s)
- Student response text

Outputs:
- Identified misconception(s)
- Explanation of the misconception
- Targeted feedback for the student
- Optional teacher-facing summary

## Design Principles

- This is a system, not just a chatbot
- AI reasoning is constrained by:
  - Standards documents
  - Known misconception patterns
  - Rubrics
- The teacher remains the final decision-maker 




## Demo Example

### Input
Expression: 10 - 2 × 4  
Student Answer: 32  
Student Work: "I did 10 minus 2 first, then multiplied."

### Output
{
    "misconception": "Left-to-right computation",
    "student_feedback": "You worked through the expression from left to right. Remember that multiplication and division must be completed before addition or subtraction. Try circling the multiplication or division first, then redo the problem.",
    "teacher_note": "Procedural misconception: student applied operations from left to right instead of following order of operations."
}
