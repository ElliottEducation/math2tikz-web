def generate_tikz_code(formula: str) -> str:
    f = formula.strip().lower()

    if f == "y = x":
        return _wrap_plot("x")
    elif f == "y = x^2":
        return _wrap_plot("x^2")
    elif f == "y = sqrt(x)":
        return _wrap_plot("sqrt(x)")
    elif f == "y = sin(x)":
        return _wrap_plot("sin(deg(x))", domain="0:2*pi")
    elif f == "y = cos(x)":
        return _wrap_plot("cos(deg(x))", domain="0:2*pi")
    elif f == "y = tan(x)":
        return _wrap_plot("tan(deg(x))", domain="0:2*pi")
    elif f == "y = e^x":
        return _wrap_plot("exp(x)")
    elif f == "y = ln(x)":
        return _wrap_plot("ln(x)", domain="0.1:4")
    elif f == "y = log(x)":
        return _wrap_plot("log10(x)", domain="0.1:4")
    elif f in ("r = sin(3θ)", "r = sin(3theta)"):
        return r"""\begin{tikzpicture}
\begin{polaraxis}
\addplot[domain=0:360,samples=300]{sin(3*x)};
\end{polaraxis}
\end{tikzpicture}"""
    else:
        return "% Unsupported function. Try something like y = sin(x)"

def _wrap_plot(expr: str, domain: str = "-2:2") -> str:
    return fr"""\begin{{tikzpicture}}
\begin{{axis}}[
    axis lines = center,
    xlabel = $x$, ylabel = $y$,
]
\addplot[domain={domain}, samples=200, color=blue] {{{expr}}};
\end{{axis}}
\end{{tikzpicture}}"""

