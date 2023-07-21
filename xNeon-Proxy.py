import os
import requests
import colorama
import concurrent.futures
import aiohttp, asyncio
from re import compile

def print_banner():
    banner = '''
                                            
\x1b[38;5;51m                                                        _.oo.
\x1b[38;5;51m                                _.u[[/;:,.         .odMMMMMM' 
\x1b[38;5;51m                             .o888UU[[[/;:-.  .o@P^    MMM^                                                         
\x1b[38;5;51m                            oN88888UU[[[/;::-.        dP^                                                          
\x1b[38;5;51m                           dNMMNN888UU[[[/;:--.   .o@P^   
\x1b[38;5;87m                          ,MMMMMMN888UU[[/;::-. o@^       
\x1b[38;5;87m                          NNMMMNN888UU[[[/~.o@P^          
\x1b[38;5;123m                          888888888UU[[[/o@^-..            
\x1b[38;5;123m                         oI8888UU[[[/o@P^:--..             
\x1b[38;5;159m                      .@^  YUU[[[/o@^;::---..              
\x1b[38;5;159m                    oMP     ^/o@P^;:::---..                
\x1b[38;5;195m                 .dMMM    .o@^ ^;::---...                  
\x1b[38;5;195m                dMMMMMMM@^`       `^^^^                    
\x1b[38;5;231m               YMMMUP^                                    
\x1b[38;5;231m                ^^    
                                    
       \x1b[38;5;51m╔═════════════════════════════════════════════════════════════╗ \x1b[38;5;255m
      \x1b[38;5;51m ║      \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━  \x1b[38;5;255mTool Get Proxy Và Check Proxy  \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━    ║\x1b[38;5;255m        
       \x1b[38;5;123m╚════╔════════════════════════════════════════════════════╗═══╝\x1b[38;5;255m
            \x1b[38;5;159m║       \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━ \x1b[38;5;255mMade By xn30n#0000 \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━ \x1b[38;5;255m═ \x1b[38;5;51m━       \x1b[38;5;159m║\x1b[38;5;255m
            \x1b[38;5;195m╚════════════════════════════════════════════════════╝\x1b[38;5;255m
            
'''
    print(banner)
    
def get_proxy():
    os.system("cd source && python ProxyScraper.py")

def check_proxy():
    os.system("cd source && python Checker.py")

def main():
    print_banner()

    while True:
        print("Nhập Lựa Chọn Của Bạn:\n\x1b[38;5;51m====\x1b[38;5;87m====\x1b[38;5;123m====\x1b[38;5;159m====\x1b[38;5;195m=====\x1b[38;5;255m")
        print("1. Get Proxy")
        print("2. Check Proxy")
        print("0. Thoát")

        choice = input("\x1b[38;5;51m====\x1b[38;5;87m====\x1b[38;5;123m====\x1b[38;5;159m====\x1b[38;5;195m=====\x1b[38;5;255m\nEnter your choice: ")

        if choice == "1":
            get_proxy()
        elif choice == "2":
            check_proxy()
        elif choice == "0":
            break
        else:
            print("Bạn Đã Nhập Sai")
    
    print("Thank you for using xNeon-Proxy!")

if __name__ == "__main__":
    main()