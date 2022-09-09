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

    # Print URL information
    print(Fore.YELLOW)
    lkas = "https://w3techs.com/sites/info/" + url
    req = requests.get(lkas).text
    soup = BeautifulSoup(req, "html.parser")
    soupx = soup.find_all("div", class_="si_tech")
    if ("Online since" in req) and ("Description on Homepage" in req):
        alexa = soupx[2].text
    elif "Description on Homepage" in req:
        alexa = soupx[1].text
    else:
        alexa = soupx[0].text
    soupz = soup.find_all("p", {"class": "si_tech"})
    front_lang = soupz[3].find("a").text
    library_lang = soupz[4].find("a").text
    websv = requests.head("https://"+url).headers.get("server")
    print("[-] Alexa Rank : %s\n[-] Front Language : %s\n[-] Library Used : %s\n[-] Web Server : %s" %
          (alexa, front_lang, library_lang, websv))
    wp = url + "/wp-admin/"
    status = requests.get("https://"+wp).status_code
    if status != 200:
        print(f"[*] Wordpress : {Fore.RED}No{Fore.WHITE}")
    else:
        print(f"[*] Wordpress : {Fore.GREEN}Yes{Fore.WHITE}")
