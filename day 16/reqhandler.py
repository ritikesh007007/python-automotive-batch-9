from collections import defaultdict, deque
import re, time, sys

THRESHOLD = 5
WINDOW_SEC = 600  # 10 min

ip_windows = defaultdict(deque)

def parse_line(line):
    match = re.search(r'(\d+\.\d+\.\d+\.\d+) .* 401', line)
    return match.group(1) if match else None

for line in sys.stdin:  # tail -f logs.txt
    ip = parse_line(line)
    if ip and 'login' in line:
        now = time.time()
        window = ip_windows[ip]
        window.append(now)
        while window and window[0] < now - WINDOW_SEC:
            window.popleft()
        if len(window) > THRESHOLD:
            print(f"ALERT: Suspicious IP {ip}: {len(window)} failures")
