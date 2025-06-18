#!/usr/bin/env python3
# bms_jacobi_check.py
# 用 SymPy 检查 center-less BMS₄ 代数 Jacobi 恒等式是否为 0

from sympy import symbols, Function, simplify

# 自变量
z = symbols('z')

# 三个生成元 Y(z), W(z), Z(z)
Y = Function('Y')(z)
W = Function('W')(z)
Z = Function('Z')(z)

def B(Q1, Q2):
    """真正的 Lie 括号：[Q1, Q2] = Q1'.Q2 - Q2'.Q1"""
    return Q1.diff(z) * Q2 - Q2.diff(z) * Q1

# 计算 Jacobi 三重括号
jacobi = B(B(Y, W), Z) + B(B(W, Z), Y) + B(B(Z, Y), W)

if __name__ == "__main__":
    print("Jacobi simplifies to:", simplify(jacobi))
