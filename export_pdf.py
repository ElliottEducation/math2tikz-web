import os
import subprocess
import tempfile

def export_to_pdf(tikz_code: str) -> str:
    """
    Converts TikZ code into a standalone LaTeX PDF and returns the path to the PDF file.
    Requires `pdflatex` to be installed on the system.
    """
    try:
        # 创建一个临时目录用于存放 .tex 和生成的 .pdf
        with tempfile.TemporaryDirectory() as temp_dir:
            tex_path = os.path.join(temp_dir, "output.tex")
            pdf_path = os.path.join(temp_dir, "output.pdf")

            # 封装完整的 LaTeX 文档模板
            latex_template = fr"""
\documentclass[tikz]{{standalone}}
\usepackage{{pgfplots}}
\pgfplotsset{{compat=1.18}}
\begin{{document}}
{tikz_code}
\end{{document}}
"""

            # 写入 .tex 文件
            with open(tex_path, "w") as tex_file:
                tex_file.write(latex_template)

            # 调用 pdflatex 编译为 PDF
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-output-directory", temp_dir, tex_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10  # 限制编译时间防止阻塞
            )

            if result.returncode == 0 and os.path.exists(pdf_path):
                return pdf_path
            else:
                print("LaTeX compilation failed:")
                print(result.stderr.decode("utf-8"))
                return None

    except Exception as e:
        print(f"[Error] export_to_pdf failed: {e}")
        return None
