import json
import re

# ----------------------------------
# Safe Evaluation
# ----------------------------------

def safe_eval(expr):
    try:
        expr = expr.replace("×", "*").replace("÷", "/")
        expr = expr.replace("(", "*(")
        return eval(expr)
    except:
        return None


# ----------------------------------
# RULES
# ----------------------------------

def rule_1_order(expression, student_work):
    if any(op in expression for op in ["*", "+", "/"]) and \
       any(w in student_work.lower() for w in ["first", "then", "add"]):

        return {
            "misconception": "Left-to-right computation",
            "student_feedback": "Use order of operations (PEMDAS).",
            "teacher_note": "Student ignoring operation priority."
        }


def rule_2_distributive(expression, student_work):
    if re.search(r"\d+\s*\(", expression):
        if "times" in student_work.lower() and "and" not in student_work.lower():
            return {
                "misconception": "Distributive property error",
                "student_feedback": "Multiply the outside number by EVERY term.",
                "teacher_note": "Distributed only to one term."
            }


def rule_3_sign(expression, student_answer):
    correct = safe_eval(expression)
    try:
        if correct is not None and float(student_answer) == -float(correct):
            return {
                "misconception": "Sign error",
                "student_feedback": "Check positive/negative signs.",
                "teacher_note": "Correct magnitude, wrong sign."
            }
    except:
        pass


def rule_4_fraction(expression):
    if "/" in expression and "+" in expression:
        return {
            "misconception": "Fraction error",
            "student_feedback": "Use a common denominator.",
            "teacher_note": "Adding top and bottom separately."
        }


def rule_5_like_terms(expression, student_work):
    if "x" in expression and "add" in student_work.lower():
        return {
            "misconception": "Combining unlike terms",
            "student_feedback": "Only combine like terms.",
            "teacher_note": "Mixing variables and constants."
        }


def rule_6_equation(expression, student_work):
    if "=" in expression and "moved" in student_work.lower():
        return {
            "misconception": "Equation error",
            "student_feedback": "Do the same to both sides.",
            "teacher_note": "Balance issue."
        }


def rule_7_variable(expression, student_work):
    if any(c.isalpha() for c in expression) and "guess" in student_work.lower():
        return {
            "misconception": "Variable confusion",
            "student_feedback": "Solve instead of guessing.",
            "teacher_note": "Misunderstands variables."
        }


def rule_8_parentheses(expression, student_work):
    if "(" in expression and "first" not in student_work.lower():
        return {
            "misconception": "Ignored parentheses",
            "student_feedback": "Solve parentheses first.",
            "teacher_note": "Skipping grouping."
        }


def rule_9_multiplication(expression, student_answer):
    if "*" in expression:
        correct = safe_eval(expression)
        try:
            if float(student_answer) != float(correct):
                return {
                    "misconception": "Multiplication error",
                    "student_feedback": "Check multiplication.",
                    "teacher_note": "Basic error."
                }
        except:
            pass


def rule_10_division(expression, student_answer):
    if "/" in expression:
        correct = safe_eval(expression)
        try:
            if float(student_answer) != float(correct):
                return {
                    "misconception": "Division error",
                    "student_feedback": "Check division.",
                    "teacher_note": "Basic error."
                }
        except:
            pass


def rule_11_multistep(student_work):
    if sum(w in student_work.lower() for w in ["then", "next", "after"]) > 2:
        return {
            "misconception": "Multi-step confusion",
            "student_feedback": "Break into smaller steps.",
            "teacher_note": "Sequence issue."
        }


def rule_12_careless(student_work):
    if len(student_work.split()) < 3:
        return {
            "misconception": "Careless error",
            "student_feedback": "Show more work.",
            "teacher_note": "Too little detail."
        }


# ----------------------------------
# MAIN ENGINE (MULTI-DETECTION)
# ----------------------------------

def analyze(expression, student_answer, student_work):

    rules = [
        lambda: rule_1_order(expression, student_work),
        lambda: rule_2_distributive(expression, student_work),
        lambda: rule_3_sign(expression, student_answer),
        lambda: rule_4_fraction(expression),
        lambda: rule_5_like_terms(expression, student_work),
        lambda: rule_6_equation(expression, student_work),
        lambda: rule_7_variable(expression, student_work),
        lambda: rule_8_parentheses(expression, student_work),
        lambda: rule_9_multiplication(expression, student_answer),
        lambda: rule_10_division(expression, student_answer),
        lambda: rule_11_multistep(student_work),
        lambda: rule_12_careless(student_work)
    ]

    results = []

    for rule in rules:
        result = rule()
        if result:
            results.append(result)

    # Final correctness check
    correct = safe_eval(expression)

    if not results:
        if str(correct) == str(student_answer):
            results.append({
                "misconception": None,
                "student_feedback": "Great job! Correct.",
                "teacher_note": "Student understands."
            })
        else:
            results.append({
                "misconception": "Unknown error",
                "student_feedback": "Check your work.",
                "teacher_note": "No clear pattern."
            })

    return results


# ----------------------------------
# TERMINAL INTERFACE
# ----------------------------------

if __name__ == "__main__":

    print("\n===ChainTheory-AI v1.0 ===")
    print("Created by James Stewart")
    print("Diagnosing how students think, one step at a time")
    print("Powered by Curiosity, The desire to learn, And the need for coffee\n")

    expression = input("Enter the math expression: ")
    student_answer = input("Enter the student's answer: ")
    student_work = input("Describe the student's work: ")

    results = analyze(expression, student_answer, student_work)

    print("\n--- Analysis Result ---")

    for i, r in enumerate(results, 1):
        print(f"\nIssue {i}:")
        print(f"Misconception: {r['misconception']}")
        print(f"Student Feedback: {r['student_feedback']}")
        print(f"Teacher Note: {r['teacher_note']}")
