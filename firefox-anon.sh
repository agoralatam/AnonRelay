#!bin/bash

clear
echo 'Running firefox with AnonRelay...'
proxychains -f proxychains_config.conf -q firefox
