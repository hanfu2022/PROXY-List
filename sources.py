import requests

SOURCES = [
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
]

def fetch_sources():
    result = set()
    for url in SOURCES:
        try:
            r = requests.get(url, timeout=15)
            for line in r.text.splitlines():
                line=line.strip()
                if ":" in line:
                    result.add(line)
        except Exception:
            pass
    return list(result)
