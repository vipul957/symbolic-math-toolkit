"""Symbolic calculus helpers with a deliberately small public API."""
from __future__ import annotations
import sympy as sp

def differentiate(expression: str, variable: str = "x") -> str:
    x = sp.Symbol(variable)
    return str(sp.diff(sp.sympify(expression), x))

def taylor(expression: str, variable: str = "x", point: float = 0, order: int = 4) -> str:
    x = sp.Symbol(variable)
    return str(sp.series(sp.sympify(expression), x, point, order).removeO())
