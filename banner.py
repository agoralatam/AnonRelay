#!bin/python3

import time
from colorama import Fore as Fr

def main_banner_move():
	line0 = [f'{Fr.GREEN}┌', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '┐']
	line1 = ['│', ' ', f'{Fr.YELLOW}S', 'C', 'R', 'I', 'P', 'T', ':', ' ', f'{Fr.GREEN}A', 'N', 'O', 'N', 'R', 'E', 'L', 'A', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '│']
	line2 = ['│', ' ', f'{Fr.YELLOW}V', 'E', 'R', 'S', 'I', 'O', 'N', ':', ' ', f'{Fr.GREEN}V', '1', '.', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '│']
	line3 = ['│', ' ', f'{Fr.YELLOW}D', 'A', 'T', 'E', ':', ' ', f'{Fr.GREEN}1', '0', '-', '1', '2', '-', '2', '0', '2', '4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '│'] 
	line4 = ['│', ' ', f'{Fr.YELLOW}C', 'O', 'D', 'E', 'D', ' ', 'B', 'Y', ' ', 'N', '4', 'S', 'S', '4', 'U', ' ', 'F', 'R', 'O', 'M', ' ', 'A', 'G', 'O', 'R', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', f'{Fr.GREEN}│']
	line5 = ['│', ' ', f'{Fr.YELLOW}T', 'E', 'L', 'E', 'G', 'R', 'A', 'M', ':', ' ', f'{Fr.GREEN}H', 'T', 'T', 'P', 'S', ':', '/', '/', 'T', '.', 'M', 'E', '/', 'A', 'G', 'O', 'R', 'A', 'L', 'A', 'T', 'A', 'M', 'C', ' ', ' ', ' ', '│']
	line6 = ['└', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', f'┘{Fr.RESET}']

	final = [line0, line1, line2, line3, line4, line5, line6]

	for i in final:
		for j in i:
			print(f"{j}", end="", flush=True)
			time.sleep(0.01)
		print("")

def main_banner_static():
        print(f"{Fr.GREEN}┌──────────────────────────────────────┐")
        print(f"│ {Fr.YELLOW}SCRIPT: {Fr.GREEN}ANONRELAY                    │")
        print(f"│ {Fr.YELLOW}VERSION: {Fr.GREEN}V1.0                        │")
        print(f"│ {Fr.YELLOW}DATE: {Fr.GREEN}10-12-2024                     │")
        print(f"│ {Fr.YELLOW}CODED BY N4SS4U FROM AGORA           {Fr.GREEN}│")
        print(f"│ {Fr.YELLOW}TELEGRAM: {Fr.GREEN}HTTPS://T.ME/AGORALATAMC   │")
        print(f"└──────────────────────────────────────┘{Fr.RESET}")

