#!/usr/bin/env python3
# test_raw_file_sizes.py

import os

# 列出要测试的 .raw 文件
RAW_FILES = [
    'DH_data/._highengphot_tf_interp.raw',
    'DH_data/lowengelec_tf_interp.raw',
]

def test_size(fn):
    print(f"Testing RAW file: {fn}")
    if not os.path.isfile(fn):
        print("  [Error] File not found\n")
        return
    size = os.path.getsize(fn)
    print(f"  [OK] Size = {size} bytes ({size/1e6:.2f} MB)\n")

if __name__ == "__main__":
    for fn in RAW_FILES:
        test_size(fn)
