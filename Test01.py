# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:30:36 2026

@author: I060878
"""
from sympy import symbols, Eq, solve
x, y = symbols('x y')
print(solve([Eq(y, x + 5), Eq(x, 5)]))   # → [{x: 5, y: 10}]