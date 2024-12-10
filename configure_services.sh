#!bin/bash

clear

# Instalando dependecias necesarias
echo -e 'Installing dependencies...'
apt install -qq tor -y > /dev/null 2>&1
apt install -qq proxychains -y > /dev/null 2>&1
apt install -qq python3 -y > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

# Creando archivo de configuracion
echo -e 'Creating configuration files...'
printf '# Config file for Proxychains\ndynamic_chain\nproxy_dns\n\ntcp_read_time_out 15000\ntcp_connect_time_out 8000\n\n[ProxyList]\nsocks5 127.0.0.1 9050\nsocks4 127.0.0.1 9050' > proxychains_config.conf
passwdtor=$(tor --hash-password FFN8N0-3NDJN38D-DDKEM39M | grep -o '16.*')
printf '#Config file for Tor\nControlPort 9051\nCookieAuthentication 1\nHashedControlPassword %s\n' "$passwdtor" > torrc

