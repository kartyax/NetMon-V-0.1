import datetime

LOG_FILE = "logs/monitor.log"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")
