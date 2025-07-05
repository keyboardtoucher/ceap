import requests
import time
from datetime import datetime

EXCHANGES = {
    "Binance": "https://api.binance.com",
    "Coinbase": "https://api.coinbase.com",
    "Kraken": "https://api.kraken.com",
    "OKX": "https://www.okx.com",
    "Bybit": "https://api.bybit.com",
    "KuCoin": "https://api.kucoin.com",
    "Bitfinex": "https://api.bitfinex.com",
    "HTX (Huobi)": "https://api.huobi.pro",
    "MEXC": "https://api.mexc.com",
    "Gate.io": "https://api.gate.io",
    "Bitget": "https://api.bitget.com",
    "Crypto.com": "https://api.crypto.com",
    "Gemini": "https://api.gemini.com",
    "BingX": "https://open-api.bingx.com",
    "Bitstamp": "https://www.bitstamp.net/api",
    "Coincheck": "https://coincheck.com/api",
    "LBank": "https://api.lbkex.com",
    "ProBit": "https://api.probit.com",
    "Phemex": "https://api.phemex.com",
    "Poloniex": "https://api.poloniex.com"
}

LOG_FILE = "ping_log.txt"

def ping_exchange(name, url, index, total, attempts=5):
    latencies = []
    print(f"\n▶ {index}/{total} - {name}")
    for i in range(attempts):
        try:
            print(f"  ↪ Request {i+1}/{attempts} ...", end=" ")
            start = time.time()
            requests.get(url, timeout=5)
            latency = (time.time() - start) * 1000  # ms
            latencies.append(latency)
            print(f"{round(latency, 1)} ms")
        except requests.exceptions.RequestException:
            latencies.append(None)
            print("failed")
        time.sleep(1)
    valid = [x for x in latencies if x is not None]
    if valid:
        avg = round(sum(valid) / len(valid), 1)
        return f"{name}: {avg} ms"
    else:
        return f"{name}: Unreachable"

def main():
    results = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results.append(f"Ping log — {timestamp}\n")

    print("📡 Starting ping test...\n")

    total = len(EXCHANGES)
    for idx, (name, url) in enumerate(EXCHANGES.items(), start=1):
        result = ping_exchange(name, url, idx, total)
        results.append(result)

    with open(LOG_FILE, "a") as f:
        f.write("\n".join(results) + "\n\n")

    print("\n✅ Test complete. Saved to ping_log.txt")

if __name__ == "__main__":
    main()