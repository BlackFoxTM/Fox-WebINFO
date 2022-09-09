import builtwith
import colorama
import pyfiglet

rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
mag = colorama.Fore.MAGENTA
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
cy = colorama.Fore.CYAN

def banner():
    figlet = pyfiglet.Figlet(font="script")
    return figlet.renderText("web info fox") 



def checker(url):
    operation = builtwith.builtwith(url)
    return ("[-] Web Server : %s\n[-] Font Script : %s\n[-] ecommerce : %s\n[-] CMS : %s\n[-] Programmed Lang With : %s\n[-] Blogs : %s" % (str(operation.get("web-servers")[0]) , str(operation.get("font-scripts")[0]) , str(operation.get("ecommerce")[0]) , str(operation.get("cms")[0]) , str(operation.get("programming-languages")[0]) , str(operation.get("blogs")[0])))

print (gn + banner())
print (rd + "[$] Coded By Maximum Radikali")
print (mag + "[+] Channel : @BlackFoxSecurityTeam")
url = input(bl + "[$] Please Enter your Url ~> ")

try:
    print (yl + checker(url) + cv)
    print (gn + "The Operation has been success")
except:
    print (rd + "The Operation has been failed , please run again")
