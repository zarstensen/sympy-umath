from sympy import Expr
from sympy.utilities.lambdify import MODULES, MATH, MATH_DEFAULT, MATH_TRANSLATIONS, lambdify

MODULES['umath'] = (MATH.copy(), MATH_DEFAULT, MATH_TRANSLATIONS, ("from uncertainties.umath import *",))

def lambdify_umath(args: list, expr: Expr, **kwargs):
    return lambdify(args, expr, modules='umath', **kwargs)
