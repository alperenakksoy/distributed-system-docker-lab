import requests, time
success = 0; failed = 0
while True:
    for url in ["http://localhost/health", "http://localhost/data/testkey"]:
        try:
            r = requests.get(url, timeout=3)
            success += 1
            print(f"{time.strftime('%H:%M:%S')} ✓ {r.status_code} {url.split('/')[-1]:10s} | ok={success} fail={failed}")
        except:
            failed += 1
            print(f"{time.strftime('%H:%M:%S')} ✗ ERROR {url.split('/')[-1]:10s} | ok={success} fail={failed}")
    time.sleep(0.5)