#!bin/bash

clear
proxychains -f proxychains_config.conf -q $@
