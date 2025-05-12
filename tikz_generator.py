import re

def generate_tikz_code(formula: str) -> str:
    f = formula.strip().lower()

    # Basic functions
    if f in ("y = x", "y = x^1"):
        return _wrap_plot("x")
    elif f == "y = x^2":
        return _wrap_plot("x^2")
    elif f == "y = x^3":
        return _wrap_plot("x^3")
    elif f == "y = sqrt(x)":
        return _wrap_plot("sqrt(x)")
    elif f.startswith("y = x^") and "^" in f:
        expr = f[4:]
        return _wrap_plot(expr)

    # Trigonometric functions
    trig_map = {
        "sin(x)": "sin(deg(x))",
        "cos(x)": "cos(deg(x))",
        "tan(x)": "tan(deg(x))",
        "-sin(x)": "-sin(deg(x))",
        "sin(x)+cos(x)": "sin(deg(x)) + cos(deg(x))",
        "tan(x)*sin(x)": "tan(deg(x)) * sin(deg(x))"
    }
    if f[4:] in trig_map:
        return _wrap_plot(trig_map[f[4:]], domain="0:2*pi")

    # Exponential and logarithmic functions
    if f == "y = e^x":
        return _wrap_plot("exp(x)")
    elif f == "y = x * e^(-x)":
        return _wrap_plot("x * exp(-x)")
    elif f == "y = ln(x)" or f == "y = log(x)":
        return _wrap_plot("ln(x)", domain="0.1:4")
    elif f == "y = ln(x+1)":
        return _wrap_plot("ln(x+1)", domain="0:4")

    # Hyperbolic functions
    if f == "y = sinh(x)":
        return _wrap_plot("sinh(x)")
    elif f == "y = cosh(x)":
        return _wrap_plot("cosh(x)")
    elif f == "y = tanh(x)":
        return _wrap_plot("tanh(x)")

    # Inverse trigonometric functions
    if f == "y = arcsin(x)":
        return _wrap_plot("deg(arcsin(x))", domain="-1:1")
    elif f == "y = arctan(x)":
        return _wrap_plot("deg(arctan(x))", domain="-5:5")

    # Absolute value
    if f == "y = |x|" or f == "y = abs(x)":
        return _wrap_plot("abs(x)")

    # Polar coordinates
    polar_map = {
        "r = sin(3θ)": "sin(3*x)",
        "r = cos(2θ)": "cos(2*x)",
        "r = 1 + cos(θ)": "1 + cos(x)"
    }
    if f in polar_map:
        return _wrap_polar(polar_map[f])

    # Parametric equations
    if f == "parametric: x = cos(t), y = sin(t)":
        return _wrap_parametric("cos(deg(x))", "sin(deg(x))")
    elif f == "parametric: x = a * cos(t), y = b * sin(t)":
        return _wrap_parametric("a * cos(deg(x))", "b * sin(deg(x))")

    # Piecewise functions
    if f.startswith("piecewise:"):
        return _wrap_piecewise([
            ("x^2", "x < 0"),
            ("x + 1", "x >= 0")
        ])

    return "% Unsupported or unrecognized function."

def _wrap_plot(expr: str, domain: str = "-2:2") -> str:
    return fr"""\begin{{tikzpicture}}
\begin{{axis}}[
    axis lines = center,
    xlabel = $x$, ylabel = $y$,
]
\addplot[domain={domain}, samples=200, color=blue] {{{{{expr}}}}};
\end{{axis}}
\end{{tikzpicture}}"""

def _wrap_polar(expr: str) -> str:
    return fr"""\begin{{tikzpicture}}
\begin{{polaraxis}}
\addplot[domain=0:360,samples=300]{{{expr}}};
\end{{polaraxis}}
\end{{tikzpicture}}"""

def _wrap_parametric(x_expr: str, y_expr: str) -> str:
    return fr"""\begin{{tikzpicture}}
\begin{{axis}}[
    axis lines = center,
    xlabel = $x$, ylabel = $y$,
]
\addplot parametric[domain=0:2*pi, samples=200] 
    ({{{x_expr}}}, {{{y_expr}}});
\end{{axis}}
\end{{tikzpicture}}"""

def _wrap_piecewise(pieces: list) -> str:
    lines = [fr"{expr}, & {cond} \\" for expr, cond in pieces]
    content = "\n".join(lines).rstrip("\\")
    return fr"""f(x) = \begin{{cases}}
{content}
\end{{cases}}"""
