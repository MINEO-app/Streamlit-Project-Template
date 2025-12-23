{
  "image_name": "",
  "docker_file": "FROM MINEO_REGISTRY/mineo_python:3.13\r\nRUN apt-get update && \\\r\n    apt-get install -y --no-install-recommends \\\r\n    curl \\\r\n    wget \\\r\n    && rm -rf /var/lib/apt/lists/*\r\n# Make sure you have requirements.txt beside this worker image file or adjust the path\r\nCOPY ../requirements.txt .\r\n\r\nRUN uv pip install --system --no-cache -r ../requirements.txt\r\nRUN uv cache clean\r\nENV PYTHONUNBUFFERED=1",
  "enabled": true,
  "description": null,
  "worker_template": "471beed7-efa1-4e8b-b8e9-4e2ed914a5a0"
}
