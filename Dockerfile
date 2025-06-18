# Dockerfile

FROM python:3.10-slim

# 安装系统依赖：wget、unzip、p7zip-full、bash
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      wget unzip p7zip-full bash && \
    rm -rf /var/lib/apt/lists/*

# 安装 Python 库
RUN pip install --no-cache-dir \
      sympy pint emcee arviz rebound toml

WORKDIR /app
COPY scripts/ ./scripts/
COPY fetch_data.sh ./

# 拉取并解压数据
RUN chmod +x fetch_data.sh && \
    ./fetch_data.sh

CMD ["bash", "-lc", "python scripts/mtheory_r4_fit.py --help"]
