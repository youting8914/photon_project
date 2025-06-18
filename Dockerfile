# Dockerfile: photon_project 一键复现环境

# 1. 基于轻量级 Python
FROM python:3.10-slim

# 2. 安装 Python 依赖
RUN pip install --no-cache-dir sympy pint emcee arviz rebound

# 3. 安装 Lean 4（nightly Linux 版）
RUN apt-get update && \
    apt-get install -y wget unzip curl && \
    wget https://github.com/leanprover/lean4/releases/download/nightly/lean-nightly-linux.tar.gz && \
    tar -xzf lean-nightly-linux.tar.gz -C /usr/local && \
    rm lean-nightly-linux.tar.gz && \
    ln -s /usr/local/lean4/bin/lean /usr/local/bin/lean

# 4. 拷贝脚本
WORKDIR /app
COPY scripts/ ./scripts/

# 5. 默认命令：显示脚本帮助
CMD ["bash", "-lc", "python scripts/mtheory_r4_fit.py --help"]
