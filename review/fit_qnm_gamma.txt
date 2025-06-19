#!/usr/bin/env python3
# fit_qnm_gamma.py
# 拟合 QNM 频率，反推 Immirzi 参数 γ

import numpy as np
from scipy.optimize import minimize

# 观测数据：模态 n vs 频率 ω_obs（示例值，需替换成真实数据）
n_obs = np.array([1, 2, 3, 4])
omega_obs = np.array([1.274, 2.548, 3.822, 5.096])

def loss(g):
    """最小二乘损失函数：拟合 ω_n = n*(1+g)"""
    return np.sum((omega_obs - n_obs * (1 + g))**2)

if __name__ == "__main__":
    res = minimize(loss, x0=0.27)
    gamma = res.x[0]
    print(f"Fitted γ = {gamma:.6f}")
