import re
import requests
import pyfiglet

from colorama import Fore
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # Print banner
    figlet = pyfiglet.Figlet(font="script")
    print(Fore.CYAN + figlet.renderText("WEB_INFO FOX"))
    print(f"{Fore.WHITE}[+] Coded By Maximum Radikali")
    print(f"{Fore.YELLOW}[+] Channel : @BlackFoxSecurityTeam")
    url = input(f"{Fore.BLUE}[&] Please Enter URL ex : (google.com) ~> ")

    # Processed URL
    resp = requests.get(f"https://w3techs.com/sites/info/{url}")
    soup = BeautifulSoup(resp.text, "html.parser")
    soupx = soup.find_all("div", class_="si_tech")

    # Find alexa rank
    if "Online since" in resp.text and "Description on Homepage" in resp.text:
        alexa = soupx[2].text
    elif "Description on Homepage" in resp.text:
        alexa = soupx[1].text
    else:
        alexa = soupx[0].text

    # Find front_lang, library_lang, websv and wordpress
    soupz = soup.find_all("p", {"class": "si_tech"})
    front_lang = soupz[3].find("a").text
    library_lang = soupz[4].find("a").text
    websv = requests.head(f"https://{url}").headers.get("server")
    resp = requests.get(f"https://{url}/wp-admin/")
    is_wordpress = f"{Fore.RED}No"

    if resp.ok:
        is_wordpress = f"{Fore.GREEN}Yes"

    # Show result
    print(f'''{Fore.YELLOW}
[-] Alexa Rank : {alexa}
[-] Front Language : {front_lang}
[-] Library Used : {library_lang}
[-] Web Server : {websv}
[*] Wordpress : {is_wordpress}{Fore.WHITE}''')
