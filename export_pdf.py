import os
import subprocess
import tempfile

def export_to_pdf(tikz_code: str) -> str:
    # Create temporary .tex file
    with tempfile.TemporaryDirectory() as temp_dir:
        tex_path = os.path.join(temp_dir, "output.tex")
        pdf_path = os.path.join(temp_dir, "output.pdf")

        latex_template = fr"""
\documentclass[tikz]{{standalone}}
\usepackage{{pgfplots}}
\pgfplotsset{{compat=1.18}}
\begin{{document}}
{tikz_code}
\end{{document}}
"""
        with open(tex_path, "w") as f:
            f.write(latex_template)

        try:
            subprocess.run(
                ["pdflatex", "-output-directory", temp_dir, tex_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return pdf_path
        except subprocess.CalledProcessError:
            return None
