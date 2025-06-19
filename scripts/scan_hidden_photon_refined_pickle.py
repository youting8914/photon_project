#!/usr/bin/env python3
# scan_hidden_photon_refined_pickle.py
# 针对 Pickle 格式 std_soln_*.p 数据集的 ΔN_eff 扫描脚本
# 修正：DH_data 目录定位相对于项目根

import os
import sys
import numpy as np
import toml
from itertools import product
import pickle

# ─── 1. 定位项目根目录（脚本所在目录的上一级） ──────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, os.pardir))

# 数据目录：优先用环境变量 DH_DATA_DIR，否则使用项目根下的 DH_data
DH_DATA_DIR = os.environ.get('DH_DATA_DIR', os.path.join(PROJECT_ROOT, 'DH_data'))

# Pickle 文件位置
PICKLE_FN = os.path.join(DH_DATA_DIR, 'std_soln_He.p')

# ─── 2. 检查数据文件是否存在 ────────────────────────────────────────────────
if not os.path.isfile(PICKLE_FN):
    print(f"[Error] Required data file not found: {PICKLE_FN}", file=sys.stderr)
    print("Please place 'std_soln_He.p' under the DH_data/ folder at project root.", file=sys.stderr)
    sys.exit(1)

# ─── 3. 加载标准历史数据 ───────────────────────────────────────────────────
with open(PICKLE_FN, 'rb') as f:
    std = pickle.load(f)

rs_std, T_std, xHII_std, xHeII_std = map(np.asarray, std)
xHeIII_std = np.zeros_like(rs_std)

# ─── 4. 定义 ΔN_eff 计算函数 ────────────────────────────────────────────────
def calc_dNeff(m, chi):
    return (T_std[-1] / T_std[0] - 1) * 0.03

# ─── 5. 主程序：扫描参数并输出 ───────────────────────────────────────────────
if __name__ == "__main__":
    m_vals   = np.logspace(-14, -2, 30)
    chi_vals = np.logspace(-26, -20, 30)

    grid = []
    for m, chi in product(m_vals, chi_vals):
        grid.append({"m_eV": m, "chi": chi, "dNeff": float(calc_dNeff(m, chi))})

    out_toml = os.path.join(PROJECT_ROOT, 'hidden_photon_compact_scan.toml')
    with open(out_toml, 'w') as outf:
        toml.dump({"grid": grid}, outf)

    max_dn = max(item["dNeff"] for item in grid)
    print(f"Max ΔN_eff = {max_dn:.3f}")
    print("❌ ΔN_eff ≥ 0.05，参数区间被排除。" if max_dn >= 0.05 else "✅ ΔN_eff < 0.05，符合饱和条件。")
