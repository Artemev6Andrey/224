#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вывести на экран большее из трёх заданных чисел"""
a, b, c = int(input()), int(input()), int(input())
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
print(mx)
