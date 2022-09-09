#!/usr/bin/python3
from requests import get, head
from pyfiglet import Figlet
from colorama import Fore
from bs4 import BeautifulSoup


if __name__ == '__main__':
    print(Fore.CYAN + Figlet(font="script").renderText("WEB_INFO FOX"))
    print(f"{Fore.WHITE}[+] Coded By Maximum Radikali")
    print(f"{Fore.YELLOW}[+] Channel : @BlackFoxSecurityTeam")
    domain = input(f"{Fore.BLUE}[&] Please Enter domain ex : (google.com) ~> ")

    resp = get(f"https://w3techs.com/sites/info/{domain}")
    soup = BeautifulSoup(resp.text, "html.parser")
    soupx = soup.find_all("div", class_="si_tech")
    alexa = soupx[0].text

    if "Online since" in resp.text and "Description on Homepage" in resp.text:
        alexa = soupx[2].text
    elif "Description on Homepage" in resp.text:
        alexa = soupx[1].text

    soupz = soup.find_all("p", {"class": "si_tech"})
    print(f'''{Fore.YELLOW}
[-] Alexa Rank : {alexa}
[-] Front Language : {soupz[3].find("a").text}
[-] Library Used : {soupz[4].find("a").text}
[-] Web Server : {head(f"https://{domain}").headers.get("server")}
[*] Wordpress : {get(f"https://{domain}/wp-admin/").ok}''')
