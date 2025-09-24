import socket
import subprocess
from module.log import log

def ping(host="8.8.8.8", count=4):
    res = subprocess.run(["ping", "-c", str(count), host], capture_output=True, text=True)
    log(res.stdout)
    times = []
    for line in res.stdout.splitlines():
        if "time=" in line:
            try:
                t = float(line.split("time=")[1].split()[0])
                times.append(t)
            except:
                pass
    return res.stdout, times

def traceroute(host="8.8.8.8"):
    res = subprocess.run(["traceroute", host], capture_output=True, text=True)
    log(res.stdout)
    return res.stdout

def port_scan(host="127.0.0.1", ports=[22, 80, 443]):
    results = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((host, port))
            results[port] = "OPEN"
        except:
            results[port] = "CLOSED"
        sock.close()
    log(str(results))
    return results
