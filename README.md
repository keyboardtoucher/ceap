# Crypto Exchange API Pinger

This is a Dockerized Python tool that measures average HTTP latency (ping) to the REST API endpoints of the top 20 centralized cryptocurrency exchanges.

## Features

- Sends 5 HTTP GET requests to each exchange's API
- Calculates average latency
- Saves results to `ping_log.txt`
- Designed to run inside Docker

## 🔧 Requirements

- Docker installed on your machine

## 🚀 Build and Run

```bash
# Clone the project
git clone <your_repo_url>
cd ping-crypto

# Build the Docker image
docker build -t crypto-ping .

# Run the container
docker run --rm -v "$(pwd)":/app crypto-ping