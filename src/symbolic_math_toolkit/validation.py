from __future__ import annotations
import sympy as sp
def numerical_derivative_check(expression, variable="x", point=.37, epsilon=1e-6):
    """Compare symbolic derivative to a central finite difference."""
    x=sp.Symbol(variable); expr=sp.sympify(expression); f=sp.lambdify(x,expr,"numpy")
    analytic=sp.lambdify(x,sp.diff(expr,x),"numpy")(point)
    numeric=(f(point+epsilon)-f(point-epsilon))/(2*epsilon)
    return float(abs(analytic-numeric))
