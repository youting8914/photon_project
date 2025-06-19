# Dockerfile

FROM python:3.10-slim

# 安装 Python 库
RUN pip install --no-cache-dir sympy pint emcee arviz rebound toml

WORKDIR /app
COPY scripts/ ./scripts/

# 默认命令：展示脚本帮助
CMD ["bash", "-lc", "python scripts/mtheory_r4_fit.py --help"]
