#!/usr/bin/env python3
# scan_hidden_photon_refined_pickle.py
# 针对 Pickle 格式 std_soln_*.p 数据集的 ΔN_eff 扫描脚本
# 增强：增加数据文件存在性检查，支持 CI 环境

import os
import sys
import numpy as np
import toml
from itertools import product
import pickle

# ─── 1. 定位脚本基本路径 ───────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 数据目录：优先使用环境变量 DH_DATA_DIR，否则默认脚本同级目录下的 DH_data
DH_DATA_DIR = os.environ.get('DH_DATA_DIR', os.path.join(BASE_DIR, 'DH_data'))

# Pickle 文件位置（Compact dataset）
PICKLE_FN = os.path.join(DH_DATA_DIR, 'std_soln_He.p')

# ─── 2. 检查数据文件存在性 ─────────────────────────────────────────────────
if not os.path.isfile(PICKLE_FN):
    print(f"[Error] Required data file not found: {PICKLE_FN}", file=sys.stderr)
    print("Please ensure you have run `fetch_data.sh` to download and extract DH_data.", file=sys.stderr)
    sys.exit(1)

# ─── 3. 加载标准历史数据：Pickle 中存储的是 (rs, Tm, xHII, xHeII) ──────────
with open(PICKLE_FN, 'rb') as f:
    std = pickle.load(f)

# 解包为四个数组
rs_std, T_std, xHII_std, xHeII_std = map(np.asarray, std)

# 如果需要 xHeIII 标量阵，用 zeros 填充（原 pickle 中未提供）
xHeIII_std = np.zeros_like(rs_std)

# ─── 4. 定义 ΔN_eff 计算代理函数 ─────────────────────────────────────────
def calc_dNeff(m, chi):
    """
    用简化的代理函数计算 ΔN_eff：
    以末端 Tm 比例变化作示例。
    """
    # 这里只示例：实际应调用 Boltzmann 或 DarkHistory
    # proxy: ΔN_eff ∝ (T_std[-1]/T_std[0] - 1) * 0.03
    return (T_std[-1] / T_std[0] - 1) * 0.03

# ─── 5. 主程序：参数扫描与结果输出 ────────────────────────────────────────
if __name__ == "__main__":
    # 构建网格参数
    m_vals   = np.logspace(-14, -2, 30)  # eV
    chi_vals = np.logspace(-26, -20, 30) # cm^3/s

    grid = []
    for m, chi in product(m_vals, chi_vals):
        dn = calc_dNeff(m, chi)
        grid.append({"m_eV": m, "chi": chi, "dNeff": float(dn)})

    # 保存结果到 TOML
    out_toml = os.path.join(BASE_DIR, 'hidden_photon_compact_scan.toml')
    with open(out_toml, 'w') as outf:
        toml.dump({"grid": grid}, outf)

    # 输出阈值检测
    max_dn = max(item["dNeff"] for item in grid)
    print(f"Max ΔN_eff = {max_dn:.3f}")
    if max_dn >= 0.05:
        print("❌ ΔN_eff ≥ 0.05，参数区间被排除。")
    else:
        print("✅ ΔN_eff < 0.05，符合饱和条件。")
