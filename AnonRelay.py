#!bin/python3

import time
import socks
import socket
import os
import requests
import sys
import subprocess
import banner
import urllib.request
from stem import Signal
from stem.control import Controller
from colorama import Fore as Fr

# --------------| Comenzar con la ejecucion de Tor
def run_tor():
    try:
        process = subprocess.Popen(["tor", "-f", "torrc"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process
    except Exception as e:
        return None


# --------------| Configurar proxy local
def config_local_proxy():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket


# --------------| Solicitar nueva ip de nodo final y recopilar los datos relacionados al nodo
def get_new_ipv4(controller):
    controller.signal(Signal.NEWNYM)

    if not controller.is_newnym_available():
        wait_time = controller.get_newnym_wait()
        time.sleep(wait_time)

    new_IP = urllib.request.urlopen("http://icanhazip.com").read().decode('utf-8').strip()
    node_data = requests.get(f"https://onionoo.torproject.org/summary?search={new_IP}")
    node_data = node_data.json().get('relays', [])
    extra_data = requests.get(f"https://ipwhois.app/json/{new_IP}")
    extra_data = extra_data.json()
    city = str(extra_data['city'])
    country = str(extra_data['country'])


    for i in node_data:
        node_name = i.get('n', 'unknown')
        ipv4 = i.get('a', ['unknown'])[0]
        ipv6 = i.get('a', ['unknown', 'unknown'])[1] if len(i.get('a', [])) > 1 else 'unknown' 
        fingerprint = i.get('f', 'unknown')

    return node_name, "socks5", ipv4, str(ipv6).replace('[', '').replace(']', ''), fingerprint, city, country

# --------------| Ejecutar en bucle hasta que el usuario cancele el proceso
def main(time_w):
    os.system("clear")
    banner.main_banner_move()
    print(f"\n {Fr.RED}[!] {Fr.YELLOW}Starting service, please wait...{Fr.RESET}")
    tor_process = run_tor()
    time.sleep(5)

    controller = Controller.from_port(port=9051)
    controller.authenticate(password='FFN8N0-3NDJN38D-DDKEM39M')

    config_local_proxy()
    time_wait = time_w
    try:
        while True:
            node_name, protocol, ipv4, ipv6, fingerprint, city, country = get_new_ipv4(controller)
            os.system("clear")
            banner.main_banner_static()

            print(f"\n {Fr.YELLOW}To run the browser use ({Fr.GREEN}bash firefox-anon.sh{Fr.YELLOW}) or ({Fr.GREEN}bash chrome-anon.sh{Fr.YELLOW}) inside the script folder from another terminal\n To run a command use ({Fr.GREEN}bash shell.sh command{Fr.YELLOW}) inside the script folder from another terminal\n\n {Fr.RED}[!] {Fr.YELLOW}To finish press CTRL + C{Fr.RESET}\n")

            print(f" {Fr.RED}[+] {Fr.YELLOW}NODE NAME: {Fr.GREEN}{node_name}")
            print(f" {Fr.RED}[+] {Fr.YELLOW}PROTOCOL: {Fr.GREEN}{protocol}")
            print(f" {Fr.RED}[+] {Fr.YELLOW}IPV4: {Fr.GREEN}{ipv4}")
            print(f" {Fr.RED}[+] {Fr.YELLOW}IPV6: {Fr.GREEN}{ipv6}")
            print(f" {Fr.RED}[+] {Fr.YELLOW}FINGERPRINT: {Fr.GREEN}{fingerprint}")
            print(f" {Fr.RED}[+] {Fr.YELLOW}LOCATION: {Fr.GREEN}{city}, {country}")

            for i in range(time_wait, 0, -1):
                if i == 1:
                        print(f"\r {Fr.RED}[+] {Fr.YELLOW}NEXT NODE: {Fr.GREEN}(switching...){Fr.RESET}", end="")
                else:
                        print(f"\r {Fr.RED}[+] {Fr.YELLOW}NEXT NODE: {Fr.GREEN}{i}{Fr.RESET}", end="")
                        time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\n{Fr.RED}! {Fr.YELLOW}Interrupted by user. Stopped AnonRelay{Fr.RESET}")
    finally:
        if tor_process:
            tor_process.terminate()

if __name__ == "__main__":
    try:
        param_time = sys.argv[1]
    except IndexError:
        print(f"\n{Fr.RED}! {Fr.YELLOW}You need to specify a time to perform the relay, {Fr.RED}example: python3 AnonRelay.py 1500{Fr.RESET}")
        sys.exit()

    if param_time == "0" or param_time == "" or param_time == None:
        print(f"\n{Fr.RED}! {Fr.YELLOW}You need to specify a time to perform the relay, {Fr.RED}example: python3 AnonRelay.py 1500{Fr.RESET}")
    elif int(param_time) < 10:
        print("\n{Fr.RED}! {Fr.YELLOW}The specified rotation time must be greater than 10{Fr.RESET}")
    else:
        main(int(param_time))
