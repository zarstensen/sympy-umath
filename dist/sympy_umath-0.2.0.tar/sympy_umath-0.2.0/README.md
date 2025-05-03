# Sympy Umath

Adds `umath` as a possible `modules` value to sympy's `lambdify` function, which uses the uncertainties package as the backend.
Also adds a `lambdify_umath` and `umath_subs` function which passes this automatically.

## Example

```python
from sympy import *
from uncertainties import *

from sympy_umath import lambdify_umath

# Setup and solve potentially complex equation
v0, g, h, t = symbols("v_0 h g t")

eq = Eq(0, h + v0 * t - Rational(1, 2) * g * t ** 2)

solutions = list(solveset(eq, t))

# Lambdify each solution with lambdify_umath.
solutions_lambda = [lambdify_umath([v0, g, h], s) for s in solutions]

print("Using lambdify_umath:")
# Evaluate the lambdified expressions with ufloat's as inputs.
for l in solutions_lambda:
    print(l(ufloat(4.2, 0.05), ufloat(9.82, 0.01), ufloat(1.6, 0.05)))

# directly evaluate using umath_subs

print("\nUsing umath_subs:")
for s in solutions:
  print(umath_subs(s, {
    v0: ufloat(4.2, 0.05),
    g: ufloat(9.82, 0.01),
    h: ufloat(1.6, 0.05)
  }))
```

```output
; Get ufloat's as output with the propagated error.

>>> Using lambdify_umath:
>>> 1.141+/-0.011
>>> -0.286+/-0.007
>>>
>>> Using umath_subs:
>>> 1.141+/-0.011
>>> -0.286+/-0.007
```

## Building

- Install poetry
  - `pip install poetry`
- Build pyproject
  - `python -m build`

Built module should now be located in a folder named `dist`.