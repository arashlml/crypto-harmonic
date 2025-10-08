FROM python:3.13-slim

WORKDIR /app

# Install build tools
RUN apt-get update && \
    apt-get install -y build-essential gfortran git curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app


RUN pip install --upgrade pip setuptools wheel


RUN pip install --no-cache-dir -r requirements.txt



CMD ["streamlit", "run", "run_backtest.py"]
