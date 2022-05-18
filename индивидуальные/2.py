<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вывести на экран большее из трёх заданных чисел"""
=======
# Вывести на экран большее из трёх заданных чисел.
>>>>>>> 33e90cf2fe22ddb85269561a9e1b1d28a5cf6781
a, b, c = int(input()), int(input()), int(input())
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
print(mx)
