#!/usr/bin/env python3
# scan_hidden_photon_refined_pickle.py
# 针对 Pickle 格式 std_soln_*.p 数据集的 ΔN_eff 扫描脚本

import os
import numpy as np
import toml
from itertools import product
import pickle

# （可选）显式设置数据目录
os.environ['DH_DATA_DIR'] = r'E:\photon_project\DH_data'

# Pickle 文件位置（Compact dataset）
PICKLE_FN = os.path.join(os.environ['DH_DATA_DIR'], 'std_soln_He.p')

# 加载标准历史数据：Pickle 中存储的是 4 元组 (rs, Tm, xHII, xHeII)，无 xHeIII
with open(PICKLE_FN, 'rb') as f:
    std = pickle.load(f)

# 解包为四个数组
rs_std, T_std, xHII_std, xHeII_std = map(np.asarray, std)

# 如果你需要 xHeIII 标量阵，可用 zeros 填充（因为原 pickle 中未提供）
xHeIII_std = np.zeros_like(rs_std)

def calc_dNeff(m, chi):
    """
    用简化的代理函数计算 ΔN_eff：
    以末端 Tm 比例变化做示例。
    """
    # 这里只示例：实际应调用 Boltzmann 或 DarkHistory
    # proxy: ΔN_eff ∝ (T_std[-1]/T_std[0] - 1) * 0.03
    return (T_std[-1] / T_std[0] - 1) * 0.03

if __name__ == "__main__":
    # 构建网格参数
    m_vals   = np.logspace(-14, -2, 30)  # eV
    chi_vals = np.logspace(-26, -20, 30) # cm^3/s

    grid = []
    for m, chi in product(m_vals, chi_vals):
        dn = calc_dNeff(m, chi)
        grid.append({"m_eV": m, "chi": chi, "dNeff": dn})

    # 保存结果
    with open("hidden_photon_compact_scan.toml", "w") as outf:
        toml.dump({"grid": grid}, outf)

    # 输出阈值检测
    max_dn = max(item["dNeff"] for item in grid)
    print(f"Max ΔN_eff = {max_dn:.3f}")
    if max_dn >= 0.05:
        print("❌ ΔN_eff ≥ 0.05，参数区间被排除。")
    else:
        print("✅ ΔN_eff < 0.05，符合饱和条件。")
