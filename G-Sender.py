from colorama import *
from colorama import init
try:
    init()
    print(Fore.GREEN + "პროგრამა დაწერილია Lord-Unknown-ის მიერ")
    print(Fore.GREEN + """ 
 ██████╗       ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝       ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║  ███╗█████╗███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║   ██║╚════╝╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚██████╔╝      ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
 ╚═════╝       ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                 
""")
    print("დაეთანხმეთ პროგრამის მოთხოვნილებებს")
    print("1) გადადით მოცემულ საიტზე: https://myaccount.google.com/lesssecureapps")
    print("2) დაეთანხმეთ Permission secure app access-ს ")
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
    print("მესიჯი წარმატებით გაიგზავნა")
except:
    print("სამწუხაროდ დაფიქსირდა შეცდომა გთხოვთ დარწმუნდეთ რომ ყოველი პარამეტრი შეგყავთ სწორად :) წარმატებები")


