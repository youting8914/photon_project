#!/usr/bin/env python3
# fit_a0_flat_debug.py
# 自动识别旋转曲线平坦区并拟合 MOND 临界加速度 a₀

import glob
import numpy as np
import math

# 请修改为你存放 .dat 文件的实际目录
DATA_DIR = r'E:\photon_project\rotmod_files'

def compute_a0(r, v, eps_factor=0.1):
    """
    自适应平坦区：eps = eps_factor * median(|dv/dr|)
    r: 半径 (m), v: 速度 (m/s)
    返回 (平均 a, 被选点索引列表)
    """
    dr = np.diff(r)
    dv = np.diff(v)
    eps = eps_factor * np.median(np.abs(dv / dr))
    idx = np.where(np.abs(dv / dr) < eps)[0] + 1
    if len(idx) < 5:
        idx = np.argsort(np.abs(dv / dr))[:5] + 1
    a_vals = v[idx]**2 / r[idx]
    return np.mean(a_vals), idx

if __name__ == "__main__":
    files = glob.glob(f"{DATA_DIR}\\*.dat")
    if not files:
        raise RuntimeError("❌ 未找到任何 rotmod*.dat 文件，请检查 DATA_DIR 是否正确。")

    a0_vals = []
    for fn in files:
        data = np.loadtxt(fn)
        r = data[:, 0] * 3.086e19   # kpc → m
        v = data[:, 1] * 1e3        # km/s → m/s
        a0, idx = compute_a0(r, v)
        print(f"{fn}: 选取 {len(idx)} 个平坦点, a0 = {a0:.3e} m/s²")
        a0_vals.append(a0)

    a0_obs = np.mean(a0_vals)
    print(f"\n共处理 {len(a0_vals)} 个星系，平均 a0_obs = {a0_obs:.3e} m/s²")

    # 理论预测
    c = 299_792_458
    Lambda = 1.1056e-52
    a0_pred = c**2 / (2 * math.pi) * math.sqrt(Lambda / 3)
    diff = (a0_obs - a0_pred) / a0_pred * 100
    print(f"理论 a0_pred = {a0_pred:.3e} m/s², 差异 = {diff:.2f} %")
