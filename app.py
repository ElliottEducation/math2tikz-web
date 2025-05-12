import streamlit as st
from tikz_generator import generate_tikz_code
from export_pdf import export_to_pdf  # PDF 导出功能

st.set_page_config(page_title="Math2TikZ", layout="wide")

st.title("Math2TikZ - Convert Math Formulas to TikZ")

with st.form("math2tikz_form"):
    user_input = st.text_input(
        "Enter a math formula (e.g., y = sin(x), y = x^2, r = sin(3θ))",
        value="y = sin(x)",
        help="Supported: y = x, x^2, sin(x), e^x, ln(x), r = sin(3θ), etc."
    )
    submitted = st.form_submit_button("Generate TikZ Code")

if submitted:
    tikz_code = generate_tikz_code(user_input)

    st.subheader("Generated TikZ LaTeX Code")
    st.code(tikz_code, language="latex")

    # 下载 .tex 文件
    st.download_button(
        label="Download as .tex file",
        data=tikz_code,
        file_name="output.tex",
        mime="text/plain"
    )

    # 生成 PDF 并提供下载按钮
    pdf_path = export_to_pdf(tikz_code)
    if pdf_path:
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download as PDF",
                data=f,
                file_name="tikz_output.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("PDF generation failed. Please ensure LaTeX is installed on the system.")
