from bs4 import BeautifulSoup
import requests
import re
import pyautogui
import webbrowser
import time
import os
import sys
from colorama import Fore
from colorama import Style
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format


def banner():
    os.system("clear")

    print("\t<=============================>")
    print("\t<===========WELCOME===========>")
    print("\t<=============================>")


def display_title_bar():
    os.system('clear')
    cprint(figlet_format('Content  Scanner'))


def end_banner():
    print(Fore.RED + '\n <================= Thankyou for using Content Scanner by Th3Blacksmith =================>')
    time.sleep(1)
    print('')
    print('''                                                                                 
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/      
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(             
             ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(                     
                 (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                       *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                           
                                     @@@@@@@@@@@@@@@@@@                             
                                      #@@@@@@@@@@@@@@@#                             
                                      @@@@@@@@@@@@@@@@@                             
                                 *&@@@@@@@@@@@@@@@@@@@@@#                          
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                           ,@@@@@@@@@@@@&/.        *#@@@@@@@@@@@@(                  
                           ,@@@@@@@@@/                 .@@@@@@@@@(                  

                                                                                   ''')
    print('')
    print(''' #######         #####  ######                                                           
    #    #    # #     # #     # #        ##    ####  #    #  ####  #    # # ##### #    # 
    #    #    #       # #     # #       #  #  #    # #   #  #      ##  ## #   #   #    # 
    #    ######  #####  ######  #      #    # #      ####    ####  # ## # #   #   ###### 
    #    #    #       # #     # #      ###### #      #  #        # #    # #   #   #    # 
    #    #    # #     # #     # #      #    # #    # #   #  #    # #    # #   #   #    # 
    #    #    #  #####  ######  ###### #    #  ####  #    #  ####  #    # #   #   #    # 
                                                                                         ''' + Style.RESET_ALL)


def print_status(status):
    print(Fore.BLUE + '<====================================================>')
    print(f'<================= {status} =================>')
    print('<====================================================>\n\n' + Style.RESET_ALL)


def process_start():
    print(Fore.BLUE + '<====================================================>')
    print('<================= Process Starting =================>')
    print('<====================================================>' + Style.RESET_ALL)
    print('')
    print('')


def process_end():
    print('')
    print('')
    print(Fore.BLUE + '<=====================================================>')
    print('<================= Process Completed =================>')
    print('<=====================================================>' + Style.RESET_ALL)


def user_choice():
    return input("\nWhat would you like to do?: ")


def options():
    print("\n[1] Run program using 'URLs.csv' and 'wordlist.txt' files.")
    print("[2] Add a url to scan list.")
    print("[3] Add a word to wordlist.")
    print("[4] View current url list")
    print("[5] View current word list")
    print("[q] Press 'q' to exit")


def scan_action(wordlist: list, urls: list):
    cwd = os.getcwd()

    for i in wordlist:
        for url in urls:
            page = requests.get(url)
            html = page.content
            soup = BeautifulSoup(html, 'html.parser')
            word = soup.body.find_all(string=re.compile(i))
            if len(word) > 0:
                print('Found matching result of ', i, ' on '+url)
                print('')
                webbrowser.open(url, 2)
                time.sleep(5)
                open(cwd + f'/screenshots/{i}.png', 'w+')
                screenshot = pyautogui.screenshot()
                screenshot.save(cwd + f'/screenshots/{i}.png')
                print('Taking screenshot and saving to screenshot folder...')
                print('')


def main():
    display_title_bar()
    options()
    
    choice = ""
    keywords = 'Keywords.txt'

    websites = 'URLs.csv'
    folder = 'screenshots'

    try:
        os.makedirs(folder, exist_ok=True)
    except Exception as e:
        print(f"There was an error creating the screenshots directory. Error: {e}")
        exit(1)

    with open(websites, encoding='utf-8-sig') as f:
        urls = [line.split()[0] for line in f]

    while choice != 'q':
        try:
            choice = user_choice()
        except KeyboardInterrupt:
            display_title_bar()
            end_banner()
            break

        if choice == '1':
            display_title_bar()
            print_status("Process Starting")
            scan_action([line.strip() for line in open(keywords, encoding='utf-8-sig')], urls)
            print_status("Process Completed")

        elif choice == '2':
            display_title_bar()
            newurl = input('\nType your new url here then press enter: ').strip()

            if newurl:
                with open('URLs.csv', 'a+') as file_object:
                    file_object.seek(0)
                    file_object.write("\n")
                    file_object.write(newurl)
                    print(Fore.GREEN + '\nupdating urls...\n' + Style.RESET_ALL)
                    time.sleep(1)
                    file_object.flush()

                with open(websites, encoding='utf-8-sig') as f:
                    urls = [line.split()[0] for line in f]
                    print('The current URLs are: \n')
                    print(Fore.YELLOW + str(urls) + Style.RESET_ALL)
                    time.sleep(1)

        elif choice == '3':
            display_title_bar()
            newwword = input('\nType your new word here then press enter: ').strip()
            if newwword:
                with open('Keywords.txt', 'a+') as file_object:
                    file_object.seek(0)
                    file_object.write("\n")
                    file_object.write(newwword)
                    print(Fore.GREEN + '\nupdating wordlist...\n' + Style.RESET_ALL)
                    time.sleep(1)
                    file_object.flush()

                wordlist = [line.strip() for line in open(keywords, encoding='utf-8-sig')]
                print('The current wordlist is: \n')
                print(Fore.YELLOW + str(wordlist) + Style.RESET_ALL)
                time.sleep(1)

        elif choice == '4':
            display_title_bar()
            print('The current URLs are: \n')
            print(Fore.YELLOW + str(urls) + Style.RESET_ALL)
            time.sleep(1)

        elif choice == '5':
            display_title_bar()
            wordlist = [line.strip() for line in open(keywords, encoding='utf-8-sig')]
            print('The current wordlist is: \n')
            print(Fore.YELLOW + str(wordlist) + Style.RESET_ALL)
            time.sleep(1)

        elif choice == 'q':
            display_title_bar()
            end_banner()

        elif choice == 'options':
            display_title_bar()
            options()

        else:
            print(Fore.RED + "\nUnknown choice, type 'options' to see a list of commands" + Style.RESET_ALL)
            time.sleep(1)


if __name__ == "__main__":
    main()

