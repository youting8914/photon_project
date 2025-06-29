#!/usr/bin/env python3
import hashlib, pathlib, urllib.request, subprocess, sys

DEST = pathlib.Path("data")
DEST.mkdir(exist_ok=True)

FILES = {
    # 1. std_soln_He.p — 正确的 raw/master 路径
    "https://raw.githubusercontent.com/hongwanliu/millicharged_DM_with_bath/master/data/std_soln_He.p": (
        "DH_data/std_soln_He.p",
        "d40ede8df9334a73cd9fd93fe518b5652d1aea55f9c63580c56a3d7543f85f63"
    ),
    # 2. rotmod_files.rar — 你的 Zenodo RAR 镜像
    "https://zenodo.org/records/15691753/files/rotmod_files.rar?download=1": (
        "rotmod_files/rotmod_files.rar",
        "8a812e9d48b1680f38d8a482aa56a9c8fc80b5832746d6b1dea6e1cd16598b52"
    ),
}

def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

for url, (relpath, expected) in FILES.items():
    dest = DEST / relpath
    if not dest.exists():
        print(f"[DL] {url.split('/')[-1]} → {dest}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, dest)
    got = sha256(dest).lower()
    if got != expected.lower():
        sys.exit(f"Hash mismatch for {dest}: got {got}, expected {expected}")
    # 如果是 .rar，就用 7z 解压
    if dest.suffix.lower() == ".rar":
        print(f"[EXTRACT] {dest} → {dest.parent}")
        subprocess.run(["7z", "x", str(dest), f"-o{dest.parent}"], check=True)
