import re

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
# CONCEPT ANALYSIS FRAMEWORK
# ----------------------------------

def build_analysis():

    return {
        "correct": False,
        "strong_concepts": [],
        "developing_concepts": [],
        "needs_support": [],
        "student_feedback": "",
        "teacher_note": ""
    }


# ----------------------------------
# UNIT 1 CONCEPTS
# ----------------------------------

def concept_1_order_of_operations(expression, student_work):

    if any(op in expression for op in ["+", "-", "*", "/"]):

        if any(word in student_work.lower()
               for word in ["first", "then", "add"]):

            return {
                "concept": "Order of Operations",
                "status": "developing"
            }

    return None


def concept_2_distributive_property(expression, student_work):

    if re.search(r"\d+\s*\(", expression):

        return {
            "concept": "Distributive Property",
            "status": "strong"
        }

    return None


def concept_3_integer_signs(expression, student_answer):

    correct = safe_eval(expression)

    try:

        if correct is not None:

            if float(student_answer) == -float(correct):

                return {
                    "concept": "Integer Signs",
                    "status": "needs_support"
                }

    except:
        pass

    return None


def concept_4_work_quality(student_work):

    if len(student_work.split()) < 3:

        return {
            "concept": "Mathematical Communication",
            "status": "needs_support"
        }

    return {
        "concept": "Mathematical Communication",
        "status": "strong"
    }


# ----------------------------------
# UNIT 2 CONCEPTS
# ----------------------------------

def concept_13_ratio_comparison(expression, student_work):

    if "/" in expression:

        return {
            "concept": "Ratio Comparison",
            "status": "developing"
        }

    return None


def concept_14_unit_rates(expression, student_work):

    if "/" in expression:

        if "per" not in student_work.lower():

            return {
                "concept": "Unit Rates",
                "status": "needs_support"
            }

    return None


# ----------------------------------
# UNIT 3 CONCEPTS
# ----------------------------------

def concept_25_percent_as_ratio(expression, student_work):

    if "%" in expression:

        return {
            "concept": "Percent as Ratio",
            "status": "strong"
        }

    return None


def concept_26_percent_to_decimal(expression, student_work):

    work = student_work.lower()

    if "%" in expression:

        if any(x in work for x in [
            "25 x",
            "50 x",
            "75 x",
            "100 x"
        ]):

            return {
                "concept": "Percent to Decimal Conversion",
                "status": "needs_support"
            }

    return None


def concept_27_percent_greater_than_100(student_work):

    work = student_work.lower()

    if "cannot be more than 100" in work:

        return {
            "concept": "Percent Greater Than 100%",
            "status": "needs_support"
        }

    return None


def concept_28_percent_less_than_1(expression):

    if "%" in expression:

        if any(x in expression for x in [
            "0.1%",
            "0.2%",
            "0.3%",
            "0.5%"
        ]):

            return {
                "concept": "Percent Less Than 1%",
                "status": "strong"
            }

    return None


def concept_29_part_whole_relationship(student_work):

    work = student_work.lower()

    if "part" in work or "whole" in work:

        return {
            "concept": "Part and Whole Relationship",
            "status": "strong"
        }

    return None


def concept_30_percent_equation(student_work):

    work = student_work.lower()

    if "percent times whole" in work:

        return {
            "concept": "Percent Equation",
            "status": "strong"
        }

    return None


def concept_31_percent_change(expression):

    if "increase" in expression.lower() or "decrease" in expression.lower():

        return {
            "concept": "Percent Change",
            "status": "developing"
        }

    return None


def concept_32_percent_error(expression):

    if "error" in expression.lower():

        return {
            "concept": "Percent Error",
            "status": "developing"
        }

    return None


def concept_33_markup(expression):

    if "markup" in expression.lower():

        return {
            "concept": "Markup",
            "status": "developing"
        }

    return None


def concept_34_markdown(expression):

    if "markdown" in expression.lower():

        return {
            "concept": "Markdown",
            "status": "developing"
        }

    return None


def concept_35_sales_tax(expression):

    if "tax" in expression.lower():

        return {
            "concept": "Sales Tax",
            "status": "developing"
        }

    return None


def concept_36_simple_interest(expression):

    if "interest" in expression.lower():

        return {
            "concept": "Simple Interest",
            "status": "developing"
        }

    return None


# ----------------------------------


# ----------------------------------
# TERMINAL MODE
# ----------------------------------

if __name__ == "__main__":

    print("\n=== ChainTheory-AI v3.0 ===\n")

    expression = input("Expression: ")
    answer = input("Student Answer: ")
    work = input("Student Explanation: ")

    result = analyze(
        expression,
        answer,
        work
    )

    print("\n--- Analysis ---")

    print("\nCorrect:")
    print(result["correct"])

    print("\nStrong Concepts:")
    for concept in result["strong_concepts"]:
        print("✓", concept)

    print("\nDeveloping Concepts:")
    for concept in result["developing_concepts"]:
        print("⚠", concept)

    print("\nNeeds Support:")
    for concept in result["needs_support"]:
        print("✗", concept)

    print("\nStudent Feedback:")
    print(result["student_feedback"])

    print("\nTeacher Note:")
    print(result["teacher_note"])
