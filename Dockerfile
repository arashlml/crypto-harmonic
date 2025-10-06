FROM python:3.13-slim

WORKDIR /app

# Install build tools
RUN apt-get update && \
    apt-get install -y build-essential gfortran git curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Create outputs folder
RUN mkdir -p /app/outputs

EXPOSE 8501

CMD ["streamlit", "run", "run_backtest.py"]
