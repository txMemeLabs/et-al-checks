# et al. sandbox probe: what can a check's code reach?
import socket, os, pathlib
def net(host, port):
    try:
        socket.create_connection((host, port), timeout=5).close()
        return "OPEN"
    except Exception as e:
        return "blocked (" + type(e).__name__ + ")"
print("NET 1.1.1.1:443", net("1.1.1.1", 443))
print("NET github.com:443", net("github.com", 443))
for f in ["/sys/fs/cgroup/cpu.max", "/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/pids.max"]:
    p = pathlib.Path(f)
    print(f, p.read_text().strip() if p.exists() else "n/a")
try:
    open("/w/x.txt", "w").write("x"); print("WRITE /w OPEN")
except Exception as e:
    print("WRITE /w blocked (" + type(e).__name__ + ")")
try:
    open("/etc/x.txt", "w").write("x"); print("WRITE /etc OPEN")
except Exception as e:
    print("WRITE /etc blocked (" + type(e).__name__ + ")")
print("USER", os.getuid())
print("RESULT=1")
