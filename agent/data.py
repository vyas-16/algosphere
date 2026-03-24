import requests

def get_crypto_prices():
    # Fetches live prices for ethereum, bitcoin and algorand
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "ethereum,bitcoin,algorand",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_defi_overview():
    # Fetches top 5 DeFi protocols and their total value locked
    url = "https://api.llama.fi/protocols"
    response = requests.get(url)
    protocols = response.json()[:5]
    summary = []
    for p in protocols:
        summary.append({
            "name": p.get("name"),
            "tvl": p.get("tvl"),
            "change_1d": p.get("change_1d")
        })
    return summary

if __name__ == "__main__":
    print("=== Crypto Prices ===")
    prices = get_crypto_prices()
    for coin, info in prices.items():
        print(f"{coin}: ${info['usd']} (24h change: {info['usd_24h_change']:.2f}%)")

    print("\n=== Top DeFi Protocols ===")
    defi = get_defi_overview()
    for p in defi:
        print(f"{p['name']}: TVL ${p['tvl']:,.0f} | 24h change: {p['change_1d']}%")