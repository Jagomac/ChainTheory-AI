import re
import json

# ----------------------------------
# SAFE EVAL
# ----------------------------------
def safe_eval(expr):
    try:
        expr = expr.replace("×", "*").replace("÷", "/")
        return eval(expr)
    except:
        return None


# ----------------------------------
# UNIT 1 CONCEPTS
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
# UNIT 2 CONCEPTS
# ----------------------------------

def rule_13_compare_totals(expression, student_work):
    if "more" in student_work.lower() and "/" in expression:
        return {
            "misconception": "Comparing totals instead of ratios",
            "student_feedback": "Compare using unit rates, not totals.",
            "teacher_note": "Comparing raw numbers."
        }

def rule_14_unit_rate(expression, student_work):
    if "/" in expression and "per" not in student_work.lower():
        return {
            "misconception": "Missing unit rate",
            "student_feedback": "Convert to a per 1 value.",
            "teacher_note": "Did not find unit rate."
        }

def rule_15_fraction_rate(expression, student_work):
    if "/" in expression and any(w in student_work.lower() for w in ["hour", "minute"]):
        return {
            "misconception": "Unit/fraction confusion",
            "student_feedback": "Check units and fractions.",
            "teacher_note": "Misinterpreting rate."
        }

def rule_16_equivalent(student_work):
    if "proportional" in student_work.lower() and "check" not in student_work.lower():
        return {
            "misconception": "Did not verify ratios",
            "student_feedback": "Check if ratios are equivalent.",
            "teacher_note": "No verification."
        }

def rule_17_overgeneral(student_work):
    if "always" in student_work.lower():
        return {
            "misconception": "Overgeneralizing",
            "student_feedback": "Not all relationships are proportional.",
            "teacher_note": "Incorrect assumption."
        }

def rule_18_proportion(expression):
    if "=" in expression and "/" in expression:
        return {
            "misconception": "Incorrect proportion use",
            "student_feedback": "Ensure ratios are equivalent.",
            "teacher_note": "Misused proportion."
        }

def rule_19_constant_k(expression):
    if "y =" in expression and "x" in expression:
        return {
            "misconception": "Missing constant k",
            "student_feedback": "Find how y relates to x.",
            "teacher_note": "Missing proportional constant."
        }

def rule_20_not_proportional(expression):
    if "y =" in expression and "+" in expression:
        return {
            "misconception": "Non-proportional equation",
            "student_feedback": "y = kx only (no +).",
            "teacher_note": "Has intercept."
        }

def rule_21_graph_origin(student_work):
    if "graph" in student_work.lower() and "origin" not in student_work.lower():
        return {
            "misconception": "Graph error",
            "student_feedback": "Graph must pass through (0,0).",
            "teacher_note": "Missing origin."
        }

def rule_22_graph_rate(student_work):
    if "point" in student_work.lower() and "/" not in student_work:
        return {
            "misconception": "Graph rate error",
            "student_feedback": "Divide y by x.",
            "teacher_note": "Did not find rate."
        }

def rule_23_additive(student_work):
    if any(w in student_work.lower() for w in ["add", "increase by"]):
        return {
            "misconception": "Additive vs multiplicative",
            "student_feedback": "Use multiplication, not addition.",
            "teacher_note": "Wrong reasoning type."
        }

def rule_24_ratio_change(student_work):
    if "ratio" in student_work.lower() and "change" in student_work.lower():
        return {
            "misconception": "Ratio misunderstanding",
            "student_feedback": "Ratios stay constant when scaled.",
            "teacher_note": "Scaling confusion."
        }


# ----------------------------------
# ANALYZE ENGINE
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
        lambda: rule_12_careless(student_work),

        # Unit 2
        lambda: rule_13_compare_totals(expression, student_work),
        lambda: rule_14_unit_rate(expression, student_work),
        lambda: rule_15_fraction_rate(expression, student_work),
        lambda: rule_16_equivalent(student_work),
        lambda: rule_17_overgeneral(student_work),
        lambda: rule_18_proportion(expression),
        lambda: rule_19_constant_k(expression),
        lambda: rule_20_not_proportional(expression),
        lambda: rule_21_graph_origin(student_work),
        lambda: rule_22_graph_rate(student_work),
        lambda: rule_23_additive(student_work),
        lambda: rule_24_ratio_change(student_work)
    ]

    results = []

    for rule in rules:
        result = rule()
        if result:
            results.append(result)

    # Final correctness
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
# TERMINAL MODE (optional)
# ----------------------------------
if __name__ == "__main__":

    print("\n=== ChainTheory-AI v2.0 ===")
    print("Diagnosing how students think, one step at a time\n")

    expression = input("Enter expression: ")
    answer = input("Student answer: ")
    work = input("Student explanation: ")

    results = analyze(expression, answer, work)

    print("\n--- Results ---")
    for r in results:
        print("\nMisconception:", r["misconception"])
        print("Student Feedback:", r["student_feedback"])
        print("Teacher Note:", r["teacher_note"])
