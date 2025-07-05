#!/bin/bash

# Output file
OUTPUT_FILE="traceroute_results.txt"
> "$OUTPUT_FILE"  # clear previous content

# List of exchanges as name-IP pairs
names=(
  "Binance" "18.164.16.116"
  "Coinbase" "104.18.25.111"
  "Kraken" "104.102.54.74"
  "OKX" "104.18.30.187"
  "Bybit" "104.18.7.218"
  "KuCoin" "104.18.25.148"
  "Bitfinex" "104.18.21.110"
  "HTX_Huobi" "47.89.190.156"
  "MEXC" "104.18.31.171"
  "Gate_io" "104.20.184.5"
  "Bitget" "104.18.3.241"
  "Crypto_com" "99.86.4.57"
  "Gemini" "104.16.132.110"
  "BingX" "47.243.75.179"
  "Bitstamp" "104.17.137.178"
  "Coincheck" "13.115.24.151"
  "LBank" "47.75.150.155"
  "ProBit" "13.225.230.45"
  "Phemex" "104.18.35.44"
  "Poloniex" "104.16.155.50"
)

# Loop over the list in steps of 2 (name + IP)
for ((i = 0; i < ${#names[@]}; i+=2)); do
  name="${names[i]}"
  ip="${names[i+1]}"

  echo "▶ $name ($ip)" | tee -a "$OUTPUT_FILE"

  # Run traceroute and prefix each hop line with the exchange name
  traceroute -n -w 1 -q 1 "$ip" 2>/dev/null | tail -n +2 | while read -r line; do
    echo "[$name] $line" | tee -a "$OUTPUT_FILE"
  done

  # Separator between exchanges
  echo -e "---\n" >> "$OUTPUT_FILE"
done