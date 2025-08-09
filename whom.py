#!/usr/bin/env python3
import argparse, os, platform, socket, subprocess, shutil
from datetime import datetime

def run(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True).strip()
    except Exception:
        return ""

def main():
    ap = argparse.ArgumentParser(description="Tiny whoami / recon")
    ap.add_argument("-t","--target", help="domain for basic DNS/HTTP (optional)")
    args = ap.parse_args()

    print("Time:", datetime.utcnow().isoformat()+"Z")
    print("User:", os.getenv("USER") or run(["whoami"]))
    print("Host:", socket.gethostname())
    print("OS:  ", platform.platform())

    # IP/iface info (Linux/macOS)
    if shutil.which("ip"):
        print("\n[ip addr]")
        print(run(["ip","addr","show"]))
    elif shutil.which("ifconfig"):
        print("\n[ifconfig]")
        print(run(["ifconfig","-a"]))

    if args.target:
        print("\n[DNS]")
        try:
            print(socket.gethostbyname_ex(args.target))
        except Exception as e:
            print("DNS error:", e)

if __name__ == "__main__":
    main()
