import smtplib
from colorama import *
from colorama import init
from getpass import getpass
try:
    init()
    print(Fore.GREEN + "Codded By Lord-Unknown")
    print(Fore.GREEN + """ 
 ██████╗       ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝       ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║  ███╗█████╗███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║   ██║╚════╝╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚██████╔╝      ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
 ╚═════╝       ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                 
""")
    print("Allow Program Permissions")
    print ("1) Go to the this site https://myaccount.google.com/lesssecureapps")
    print("2) Give Permission secure app access ")
   
    username = input("Your Gmail: ")
    password = getpass()
    c = input("Send to: ")
    msg = input("Message: ")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(username,c, msg)
    server.quit()
    print("Sent Succsesfully")
except:
    print("Not Sent")


