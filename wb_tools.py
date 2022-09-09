import requests
from bs4 import BeautifulSoup
import re
import colorama
import pyfiglet

rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
mag = colorama.Fore.MAGENTA
gn = colorama.Fore.GREEN
bl = colorama.Fore.BLUE
yl = colorama.Fore.YELLOW
cy = colorama.Fore.CYAN


def banner():
    figlet = pyfiglet.Figlet(font="script")
    return figlet.renderText("WEB_INFO FOX")


#site = "https://w3techs.com/sites/info/000webhost.com"

def checker(site):
    print (yl)
    lkas = "https://w3techs.com/sites/info/" + site
    req = requests.get(lkas).text
    soup = BeautifulSoup(req , "html.parser")
    soupx = soup.find_all("div",class_="si_tech")
    if ("Online since"  in req) and ("Description on Homepage" in req):
        alexa = soupx[2].text
    elif "Description on Homepage" in req:
        alexa = soupx[1].text
    else:
        alexa = soupx[0].text
    soupz = soup.find_all("p" , {"class":"si_tech"})
    front_lang = soupz[3].find("a").text
    library_lang = soupz[4].find("a").text
    websv = requests.head("https://"+site).headers.get("server")
    print ("[-] Alexa Rank : %s\n[-] Front Language : %s\n[-] Library Used : %s\n[-] Web Server : %s" % (alexa , front_lang , library_lang , websv))
    wp = site + "/wp-admin/"
    status = requests.get("https://"+wp).status_code
    if status != 200:
        print (f"[*] Wordpress : {rd}No{cv}")
    else:
        print (f"[*] Wordpress : {gn}Yes{cv}")


print (cy + banner())
print (mag + "[+] Coded By Maximum Radikali")
print (yl + "[+] Channel : @BlackFoxSecurityTeam")
url = input(bl + "[&] Please Enter URL ex : (google.com) ~> ")
checker(url)
