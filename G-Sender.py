from colorama import *
import pyfiglet
print(Fore.GREEN + "Codded By Cheater")
print (Fore.GREEN + "=================================================================")
a = pyfiglet.figlet_format("Gmail-Sender")
print (a)
print (Fore.GREEN + "=================================================================")
try:
    print("Allow Program Permissions")
    print ("1) Go to the this site https://myaccount.google.com/lesssecureapps")
    print("2) Give Permission secure app access ")
    import smtplib
    from getpass import getpass
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


