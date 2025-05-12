import streamlit as st
from tikz_generator import generate_tikz_code

st.set_page_config(page_title="Math2TikZ", layout="wide")

st.title("Math2TikZ - Convert Math Formulas to TikZ")

with st.form("math2tikz_form"):
    user_input = st.text_input(
        "Enter a math formula (e.g., y = sin(x), y = x^2, r = sin(3θ))",
        value="y = sin(x)",
        help="Supported types: linear, quadratic, trig, exponential, polar"
    )
    submitted = st.form_submit_button("Generate TikZ Code")

if submitted:
    tikz_code = generate_tikz_code(user_input)
    st.subheader("Generated TikZ LaTeX Code")
    st.code(tikz_code, language="latex")

    st.download_button(
        label="Download as .tex file",
        data=tikz_code,
        file_name="output.tex",
        mime="text/plain"
    )
