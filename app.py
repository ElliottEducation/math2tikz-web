import streamlit as st
from tikz_generator import generate_tikz_code

# 可改为 Supabase 登录逻辑判断
is_pro_user = False  # 设置为 True 可测试 Pro 界面功能

st.set_page_config(page_title="Math2TikZ", layout="wide")

st.title("Math2TikZ - Convert Math Formulas to TikZ")

# 功能说明 / 引导区块
with st.expander("ℹ️ How to use Math2TikZ", expanded=False):
    st.markdown("""
**Supported formula formats:**
- `y = x`, `y = x^2`, `y = sqrt(x)`
- `y = sin(x)`, `cos(x)`, `tan(x)`
- `y = e^x`, `ln(x)`, `log(x)`
- `r = sin(3θ)` (polar plot)

**Main features:**
- Convert math formula to TikZ LaTeX code
- Download as `.tex`
- [Pro only] PDF output (requires local LaTeX)

**Coming soon:**
- Image preview rendering
- OCR: image → formula
- Pro login & export history
""")

# 主输入表单
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

    # 一键复制区域
    st.text_area("Click below to copy", tikz_code, height=150)
    st.markdown("Copy manually or use download/export options below.")

    # 下载 .tex 文件
    st.download_button(
        label="Download as .tex file",
        data=tikz_code,
        file_name="output.tex",
        mime="text/plain"
    )

    # PDF 提示（Pro 专属）
    if is_pro_user:
        st.markdown("**PDF export is available only when running locally with LaTeX installed.**")
    else:
        st.warning("⚠️ PDF export is a Pro-only feature. Please upgrade to access.")

    # TikZ 示例图预览（仅 y = sin(x) 示意）
    st.subheader("Preview (for demonstration only)")
    if "sin" in user_input:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Sine_function.svg/500px-Sine_function.svg.png",
            caption="Approximate preview of y = sin(x)"
        )
    else:
        st.info("Preview currently available only for y = sin(x).")
