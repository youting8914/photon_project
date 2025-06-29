#!/usr/bin/env python3
import hashlib, pathlib, urllib.request, subprocess, sys

DEST = pathlib.Path("data")
DEST.mkdir(exist_ok=True)

FILES = {
    # 1) DH_data/std_soln_He.p：GitHub RAW (master branch)
    "https://raw.githubusercontent.com/hongwanliu/millicharged_DM_with_bath/master/data/std_soln_He.p": (
        "DH_data/std_soln_He.p",
        "d40ede8df9334a73cd9fd93fe518b5652d1aea55f9c63580c56a3d7543f85f63"
    ),
    # 2) rotmod_files.rar：Zenodo 镜像 (CC BY 4.0):contentReference[oaicite:0]{index=0}
    "https://zenodo.org/records/15691753/files/rotmod_files.rar?download=1": (
        "rotmod_files/rotmod_files.rar",
        "0e986900ed810f1ad750b2f43e39cba8c2485a992edacd18979532a05d1e898f"
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
    # 若为 RAR，使用 7z 解压
    if dest.suffix.lower() == ".rar":
        print(f"[EXTRACT] {dest} → {dest.parent}")
        subprocess.run(["7z", "x", str(dest), f"-o{dest.parent}"], check=True)
