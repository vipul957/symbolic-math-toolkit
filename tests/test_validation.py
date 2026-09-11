from symbolic_math_toolkit.validation import numerical_derivative_check
def test_check(): assert numerical_derivative_check("x**2",.4) < 1e-5
