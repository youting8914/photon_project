#!/usr/bin/env python3
# test_text_csv_files.py

import os
import pandas as pd

# 列出要测试的文本和 CSV 文件
TEXT_CSV_FILES = [
    'DH_data/boost_data.txt',
    'DH_data/CMB_limits_phot_decay.csv',
    'DH_data/dlNdlxIEW_coords_table.txt',
]

def test_table(fn):
    print(f"Testing Text/CSV file: {fn}")
    if not os.path.isfile(fn):
        print("  [Error] File not found\n")
        return
    try:
        # pandas 自动探测分隔符
        df = pd.read_csv(fn, sep=None, engine='python')
        print(f"  [OK] Shape = {df.shape}\n")
    except Exception as e:
        print(f"  [Fail] Exception: {e}\n")

if __name__ == "__main__":
    for fn in TEXT_CSV_FILES:
        test_table(fn)
