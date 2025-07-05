FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy script
COPY ping_cryptos.py /app/ping_cryptos.py
WORKDIR /app

CMD ["python", "-u", "ping_cryptos.py"]