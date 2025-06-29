#!/usr/bin/env python3
import hashlib, pathlib, urllib.request, subprocess, sys, tarfile

# 下载目标根目录
DEST = pathlib.Path("data")
DEST.mkdir(exist_ok=True)

# 要下载的文件及其 SHA-256 校验值
FILES = {
    # 1）DH_data/std_soln_He.p：GitHub raw（锁定 commit）
    "https://raw.githubusercontent.com/hongwanliu/millicharged_DM_with_bath/1d7148d/data/std_soln_He.p": (
        "DH_data/std_soln_He.p",
        "d40ede8df9334a73cd9fd93fe518b5652d1aea55f9c63580c56a3d7543f85f63"
    ),
    # 2）rotmod_files.tar.gz：Zenodo 镜像
    "https://zenodo.org/records/15691753/files/rotmod_files.tar.gz?download=1": (
        "rotmod_files/rotmod_files.tar.gz",
        "8a812e9d48b1680f38d8a482aa56a9c8fc80b5832746d6b1dea6e1cd16598b52"
    ),
}

def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

for url, (rel, expected) in FILES.items():
    dest = DEST / rel
    if not dest.exists():
        print(f"[DL] {url.split('/')[-1]} → {dest}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, dest)
    got = sha256(dest).lower()
    if got != expected.lower():
        sys.exit(f"Hash mismatch for {dest}: got {got}, expected {expected}")
    # 如果是 .tar.gz，则解压
    if dest.suffixes[-2:] == ['.tar', '.gz']:
        print(f"[EXTRACT] {dest} → {dest.parent}")
        with tarfile.open(dest) as tar:
            tar.extractall(path=dest.parent)
