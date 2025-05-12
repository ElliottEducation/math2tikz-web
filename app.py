import streamlit as st
from tikz_generator import generate_tikz_code
from auth import sign_in, sign_up, get_user_role
from user_state import init_user_state, save_formula_to_history

# Initialize login state and history
init_user_state()

# Sidebar login/register form
with st.sidebar:
    st.title("Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    mode = st.radio("Action", ["Login", "Register"], horizontal=True)
    if st.button("Submit"):
        if email and password:
            if mode == "Login":
                result = sign_in(email, password)
                if result.get("user"):
                    st.session_state.user = result["user"]
                    st.session_state.role = get_user_role(result["user"])
                    st.success("Login successful")
                else:
                    st.error("Login failed.")
            else:
                result = sign_up(email, password)
                if result.get("user"):
                    st.session_state.user = result["user"]
                    st.session_state.role = get_user_role(result["user"])
                    st.success("Registration successful")
                else:
                    st.error("Signup failed.")
        else:
            st.warning("Please enter both email and password")

# User center display
if st.session_state.user:
    st.sidebar.markdown("---")
    st.sidebar.write(f"**Logged in as:** {st.session_state.user['email']}")
    st.sidebar.write(f"**Role:** {st.session_state.role}")
    if st.session_state.history:
        st.sidebar.markdown("**History:**")
        for h in st.session_state.history[-5:][::-1]:
            st.sidebar.code(h)

# Main app area
st.set_page_config(page_title="Math2TikZ", layout="wide")
st.title("Math2TikZ - Convert Math Formulas to TikZ")

with st.expander("ℹ️ Supported Functions", expanded=False):
    st.markdown("""
**Examples:**
- `y = x^2`, `y = sqrt(x)`
- `y = sin(x)`, `y = x * e^(-x)`
- `r = sin(3θ)`, `parametric: x = cos(t), y = sin(t)`
- `piecewise: x^2 if x<0; x+1 if x>=0`
""")

with st.form("input_form"):
    user_input = st.text_input("Enter a formula:", value="y = sin(x)")
    submitted = st.form_submit_button("Generate TikZ")

if submitted:
    tikz_code = generate_tikz_code(user_input)
    save_formula_to_history(user_input)

    st.subheader("TikZ LaTeX Output")
    st.code(tikz_code, language="latex")

    st.text_area("Copy:", tikz_code, height=150)
    st.download_button("Download .tex", data=tikz_code, file_name="output.tex", mime="text/plain")

    if st.session_state.role == "pro":
        st.markdown("**[Pro] PDF export supported locally.**")
    else:
        st.warning("PDF export is for Pro users only.")
        st.button("Upgrade to Pro")

    st.subheader("Preview")
    if "sin" in user_input:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Sine_function.svg/500px-Sine_function.svg.png",
                 caption="Preview: y = sin(x)")
    else:
        st.info("Preview available only for selected functions.")
