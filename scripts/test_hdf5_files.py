#!/usr/bin/env python3
# scripts/test_hdf5_files.py

import os
import h5py

# ─── 1. 定位项目根目录 ────────────────────────────────────────────────
THIS_DIR = os.path.dirname(os.path.abspath(__file__))   # .../photon_project/scripts
PROJECT_ROOT = os.path.dirname(THIS_DIR)                # .../photon_project

# ─── 2. 列出要测试的 HDF5 文件（位于 DH_data/ 下） ────────────────────
HDF5_FILES = [
    os.path.join(PROJECT_ROOT, 'DH_data', 'f_std.h5'),
    os.path.join(PROJECT_ROOT, 'DH_data', 'binning.h5'),
    os.path.join(PROJECT_ROOT, 'DH_data', 'He_exc_xsec_data.h5'),
]

def test_h5(fn):
    print(f"Testing HDF5 file: {fn}")
    if not os.path.isfile(fn):
        print("  [Error] File not found\n")
        return
    try:
        with h5py.File(fn, 'r') as f:
            keys = list(f.keys())
        print(f"  [OK] Top-level groups/datasets: {keys}\n")
    except Exception as e:
        print(f"  [Fail] Exception: {e}\n")

if __name__ == "__main__":
    for fn in HDF5_FILES:
        test_h5(fn)
