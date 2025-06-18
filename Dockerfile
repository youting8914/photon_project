# Dockerfile: photon_project 一键复现环境

FROM python:3.10-slim

# 安装 Python 依赖
RUN pip install --no-cache-dir sympy pint emcee arviz rebound toml


# 拷贝脚本
WORKDIR /app
COPY scripts/ ./scripts/

# 默认命令：展示脚本帮助
CMD ["bash", "-lc", "python scripts/mtheory_r4_fit.py --help"]
