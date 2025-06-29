#!/usr/bin/env python3
import hashlib, pathlib, urllib.request, subprocess, sys, tarfile

# 下载目标根目录
DEST = pathlib.Path("data")
DEST.mkdir(exist_ok=True)

# 要下载的文件及其 SHA256 校验
FILES = {
    # 1. DH_data/std_soln_He.p: 锁定到特定 commit 的 raw 链接
    "https://raw.githubusercontent.com/hongwanliu/millicharged_DM_with_bath/1d7148d/data/std_soln_He.p":
        ("DH_data/std_soln_He.p",
         "d40ede8df9334a73cd9fd93fe518b5652d1aea55f9c63580c56a3d7543f85f63"),

    # 2. rotmod_files.tar.gz: 你在 Zenodo 上传的镜像
    "https://zenodo.org/records/15691753/files/rotmod_files.tar.gz?download=1":
        ("rotmod_files/rotmod_files.tar.gz",
         "8a812e9d48b1680f38d8a482aa56a9c8fc80b5832746d6b1dea6e1cd16598b52"),
}

def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

for url, (rel_path, expected) in FILES.items():
    dest_path = DEST / rel_path
    if not dest_path.exists():
        print(f"[DL] {url} → {dest_path}")
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, dest_path)
    # 校验哈希
    h = sha256(dest_path)
    if h.lower() != expected.lower():
        sys.exit(f"Hash mismatch for {dest_path}: got {h}, expected {expected}")
    # 对 tar.gz 解压
    if dest_path.suffixes[-2:] == ['.tar', '.gz']:
        print(f"[EXTRACT] {dest_path} → {dest_path.parent}")
        with tarfile.open(dest_path) as tar:
            tar.extractall(path=dest_path.parent)
