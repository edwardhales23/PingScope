
#### **ping.py**
```python
import subprocess
import sys

def ping(host, count=5):
    cmd = ["ping", "-c", str(count), host]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Ping results:\n{result.stdout}")
    else:
        print(f"Failed to reach {host}")

if len(sys.argv) > 1:
    ping(sys.argv[1])
else:
    print("Usage: python ping.py <hostname>")
