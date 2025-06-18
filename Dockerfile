# Dockerfile

FROM python:3.10-slim

# 1. 安装系统依赖：wget、unzip、unrar
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      wget unzip unrar && \
    rm -rf /var/lib/apt/lists/*

# 2. 安装 Python 库
RUN pip install --no-cache-dir \
      sympy pint emcee arviz rebound toml

# 3. 拷贝脚本与数据拉取脚本
WORKDIR /app
COPY scripts/ ./scripts/
COPY fetch_data.sh ./

# 4. 赋予执行权限并拉取数据
RUN chmod +x fetch_data.sh && \
    ./fetch_data.sh

# 5. 默认命令：展示脚本帮助
CMD ["bash", "-lc", "python scripts/mtheory_r4_fit.py --help"]
