import streamlit as st
from tikz_generator import generate_tikz_code

# Placeholder for future login logic (e.g., via Supabase)
is_pro_user = False

# Set Streamlit page configuration
st.set_page_config(page_title="Math2TikZ", layout="wide")

# App title
st.title("Math2TikZ - Convert Math Formulas to TikZ")

# Collapsible usage instructions
with st.expander("ℹ️ How to use Math2TikZ", expanded=False):
    st.markdown("""
**Supported formula formats:**

- **Basic functions:**  
  `y = x`, `x^2`, `sqrt(x)`, `x^3`, `x * e^(-x)`
  
- **Trigonometric:**  
  `y = sin(x)`, `cos(x)`, `tan(x)`, combinations
  
- **Exponential / Logarithmic:**  
  `e^x`, `ln(x)`, `ln(x+1)`, `log(x)`
  
- **Hyperbolic:**  
  `sinh(x)`, `cosh(x)`, `tanh(x)`
  
- **Inverse trig:**  
  `arcsin(x)`, `arctan(x)`
  
- **Absolute:**  
  `|x|`, `abs(x)`
  
- **Polar curves:**  
  `r = sin(3θ)`, `r = cos(2θ)`, `r = 1 + cos(θ)`
  
- **Parametric:**  
  `parametric: x = cos(t), y = sin(t)`
  
- **Piecewise:**  
  `piecewise: x^2 if x < 0; x+1 if x >= 0`

**Main features:**
- Convert formula to TikZ LaTeX code
- Download as `.tex`
- [Pro only] PDF export (requires local LaTeX)

**Coming soon:**
- TikZ image rendering
- Image OCR (formula recognition)
- Pro account system
""")

# Input form
with st.form("math2tikz_form"):
    user_input = st.text_input(
        "Enter a math formula:",
        value="y = sin(x)",
        help="Try y = x^2, y = ln(x), r = sin(3θ), or piecewise: ..."
    )
    submitted = st.form_submit_button("Generate TikZ Code")

if submitted:
    tikz_code = generate_tikz_code(user_input)

    st.subheader("Generated TikZ LaTeX Code")
    st.code(tikz_code, language="latex")

    # Manual copy block
    st.text_area("Copy to clipboard:", tikz_code, height=150)
    st.markdown("Copy manually or use the buttons below:")

    # Download .tex file
    st.download_button(
        label="Download as .tex",
        data=tikz_code,
        file_name="output.tex",
        mime="text/plain"
    )

    # PDF output notice (Pro only)
    if is_pro_user:
        st.markdown("**PDF export is available only in local environments with LaTeX.**")
    else:
        st.warning("⚠️ PDF export is available for Pro users only.")
        st.button("Upgrade to Pro")

    # Optional preview image
    st.subheader("Preview (placeholder)")
    if "sin" in user_input:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Sine_function.svg/500px-Sine_function.svg.png",
            caption="Preview: y = sin(x)"
        )
    else:
        st.info("Preview available only for selected demo functions.")
