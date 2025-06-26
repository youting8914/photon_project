#!/usr/bin/env python3
import pathlib, urllib.request, hashlib, tarfile, sys

DEST = pathlib.Path("data")
DEST.mkdir(exist_ok=True)

files = {
    # url                                   : (local path, sha256)
    "https://raw.githubusercontent.com/hongwanliu/millicharged_DM_with_bath/master/data/std_soln_He.p":
        (DEST/"DH_data/std_soln_He.p",
         "ed33184c1a..."),   # <填入官方檔案雜湊>
    "https://kapteyn.phys.rug.nl/gipsy/examples/rotmod.tar.gz":
        (DEST/"rotmod_files/rotmod.tar.gz",
         "8a812e9d48..."),
}

for url, (path, sha) in files.items():
    if path.exists():
        print(f"[skip] {path} 已存在")
        continue
    print(f"[DL] {url} → {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, path)
    # 驗證雜湊
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    if h != sha:
        sys.exit(f"Hash mismatch for {path}")

# 可選：解壓 rotmod
rot = DEST/"rotmod_files/rotmod.tar.gz"
if rot.exists():
    with tarfile.open(rot) as tar:
        tar.extractall(path=DEST/"rotmod_files")
