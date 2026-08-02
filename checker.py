import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def check(proxy):
    try:
        r=requests.get(
            "https://www.google.com",
            proxies={"http":"http://"+proxy},
            timeout=5
        )
        if r.status_code < 500:
            return proxy
    except Exception:
        pass

def check_all(items):
    out=[]
    with ThreadPoolExecutor(max_workers=80) as ex:
        jobs=[ex.submit(check,x) for x in items]
        for j in as_completed(jobs):
            r=j.result()
            if r:
                out.append(r)
    return out
