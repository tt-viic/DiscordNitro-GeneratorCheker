from time import *
from discord_webhook import DiscordWebhook
import json, subprocess, random, string, time, requests, colorama, ctypes, os
import requests
import rainbowtext

colors = {\
    'B' : '\033[94m',
     'OKGREEN' : '\033[92m',
    'WARNING' : '\033[93m',
    'RED' : '\033[1;31;40m',
    'reset':'\033[0m'
}

def colorText(text):
    for color in colors:
        text = text.replace("[[" + color + "]]", colors[color])
    return text

def Main(): 
    reset = '[[reset]]'          
    banner1=('''
            [[B]]███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
            ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
            ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
            ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
            ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
            ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
            ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
                ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
                    ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░
    [[reset]]''')
    banner2=('''                
                        ╔═════════════════════════════════════════════════════════╗
                        ║                      Nitro Tool by viic                 ║
                        ║═════════════════════════════════════════════════════════║
                        ║ [1] NITRO CODE GENERADOR                                ║
                        ║ [2] NITRO CODE CHECKER                                  ║ 
                        ║ [E] EXIT                                                ║
                        ╚═════════════════════════════════════════════════════════╝        
    ''')
    print(colorText(banner1))
    print((rainbowtext.text(banner2)))
    print(colorText(reset))
    h = input('escoja la herramienta que desea utilizar> ') 
    if h == '1':
        Gen()

    elif h == '2':
        Checker()


def Checker():
    checked = 0
    valido = 0
    invalido = 0
    f=open("codes.txt","r+", encoding='utf-8')
    v=open("valid_codes.txt","a", encoding='utf-8')

    for line in f:
        nitro = line.strip("\n")
        
        url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(colorText('[[OKGREEN]][VALIDO][[reset]]'+str(nitro)))        
            v.write(f"{nitro}\n")
            checked += 1
            valido += 1
        else:
            print(colorText(f'[[RED]][INVALIDO][[reset]]{nitro}'))
            checked += 1
            invalido += 1

    f.close()
    v.close()
    print(f"\nSe checkearon códigos nitro,[[OKGREEN]]{valido} Validos[[reset]] y [[RED]]{invalido} Invalidos[[reset]]\n")
    input(f"   Presione cualquier tecla para volver al Menu de Inicio")
    Main()


def Gen():
        num=int(input(f"¿Cuantos códigos desea generar? "))
        path = str(os.getcwd())+"/" + "codes.txt"
        contador = 1
        start = time.time()

        while contador <= num:
            f=open("codes.txt","a", encoding='utf-8')    
            nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            f.write(nitro+'\n')
            print(nitro)
            f.close()
            contador += 1
            
        end = time.time()
        input(f"\n   Presiona cualquier tecla para volver al Menó de Inicio.")
        print(end-start)
        if input == input:
            Main()
                
                

Main()
    
