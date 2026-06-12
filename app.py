import streamlit as st
from EDUSense_engine import analyze

# --------------------------------------------------
# DESIGN NOTE (Phase 2 - Intent Inference)
#
# EDUSense is reasoning-first, not a calculator.
# Student input may be an expression, an answer,
# an explanation, or a mix of all three.
#
# Before analyzing misconceptions or correctness,
# the system must infer student intent:
#   - expression (working)
#   - answer (asserting a result)
#   - explanation (describing thinking)
#
# Symbol normalization (x, X, ×, (), adjacency)
# happens BEFORE intent inference.
#
# Do NOT auto-compute expressions.
# --------------------------------------------------

st.set_page_config(page_title="EDUSense-AI", layout="centered")

# ----------------------------
# Helper: Normalize student math representations
# ----------------------------
def normalize_expression(text):
    if not text:
        return text

    normalized = text

    # Normalize multiplication symbols
    normalized = normalized.replace("×", "*")
    normalized = normalized.replace("X", "*")
    normalized = normalized.replace("x", "*")

    # Handle implicit multiplication
    normalized = normalized.replace(") ", ")*")
    normalized = normalized.replace(")(", ")*(")

    return normalized


# ----------------------------
# Helper: Infer student intent
# ----------------------------
def infer_intent(text):
    if not text:
        return "unknown"

    lowered = text.lower()

    has_math_symbols = any(sym in text for sym in ["*", "+", "-", "/", "(", ")"])
    has_equals = "=" in text
    has_words = any(word in lowered for word in [
        "i", "because", "then", "first", "next",
        "thought", "did", "added", "multiplied"
    ])

    if has_equals and has_math_symbols:
        return "answer_assertion"
    elif has_words and has_math_symbols:
        return "mixed_reasoning"
    elif has_words:
        return "explanation"
    elif has_math_symbols:
        return "expression"
    else:
        return "unknown"
