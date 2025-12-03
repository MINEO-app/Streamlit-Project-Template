FROM MINEO_REGISTRY/mineo_python:3.13
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*
# Make sure you have requirements.txt beside this worker image file or adjust the path
COPY requirements.txt .

RUN uv pip install --system --no-cache -r requirements.txt
RUN uv cache clean
ENV PYTHONUNBUFFERED=1
