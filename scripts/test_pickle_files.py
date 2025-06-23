#!/usr/bin/env python3
# test_pickle_files.py

import os
import pickle

# 列出要测试的 .p 文件相对项目根路径
PICKLE_FILES = [
    'DH_data/std_soln_He.p',
    'DH_data/f_elec_decay_std.p',
    'DH_data/f_phot_swave_std.p',
]

def test_pickle(fn):
    print(f"Testing Pickle file: {fn}")
    if not os.path.isfile(fn):
        print("  [Error] File not found\n")
        return
    try:
        with open(fn, 'rb') as f:
            data = pickle.load(f)
        print(f"  [OK] Loaded type {type(data)} with length {len(data)}\n")
    except Exception as e:
        print(f"  [Fail] Exception: {e}\n")

if __name__ == "__main__":
    for fn in PICKLE_FILES:
        test_pickle(fn)
