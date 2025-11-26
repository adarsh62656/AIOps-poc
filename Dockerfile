# Dockerfile
FROM pytorch/pytorch:2.2.0-cuda11.8-cudnn8-runtime as base

WORKDIR /app
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

COPY server.py .

# Expose port for FastAPI
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]
