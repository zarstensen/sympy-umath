from sympy import Expr
from sympy.utilities.lambdify import MODULES, MATH_TRANSLATIONS, lambdify

UMATH_DEFAULT = {}

UMATH = UMATH_DEFAULT.copy()

UMATH_TRANSLATIONS = MATH_TRANSLATIONS.copy()

MODULES['umath'] = (UMATH, UMATH_DEFAULT, UMATH_TRANSLATIONS, ("from math import *", "from uncertainties.umath import *",))

def lambdify_umath(args: list, expr: Expr, **kwargs):
    return lambdify(args, expr, modules='umath', **kwargs)

def umath_subs(expr: Expr, subs: dict):
    return lambdify_umath(list(subs.keys()), expr)(*subs.values())
    
