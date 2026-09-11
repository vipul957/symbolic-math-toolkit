from symbolic_math_toolkit.calculus import differentiate, taylor

def test_derivative(): assert differentiate("x**3 + 2*x") == "3*x**2 + 2"

def test_taylor(): assert "x**2/2" in taylor("exp(x)", order=3)
