from datetime import datetime
import subprocess
import time
import random

services = ["backend", "redis", "nginx"]
totalDuration = 600
start_time = time.time()

def now():
    return datetime.now().strftime("%H:%M:%S")

print(f"{now()}: Fault Injection starting...")

while time.time() - start_time < totalDuration:
    target = random.choice(services)

    print(f"{now()}: Killing service -> {target}")
    subprocess.run(["docker-compose", "kill", target])

    print(f"{now()}: Waiting 10 seconds (downtime)...")
    time.sleep(10)

    print(f"{now()}: Restarting service -> {target}")
    subprocess.run(["docker-compose", "start", target])

    print(f"{now()}: Waiting 50 seconds until next cycle...")
    time.sleep(50)

print(f"{now()}: Fault injection complete.")