import os
choose = input("choose os: 1)debian/ubuntu, 2)arch: ")
if choose == 1:
  os.system("sudo apt install python3-pip")
  os.system("pip3 install colorama")
if choose == 2"
os.system("sudo pacman -Sy  pip")
os.system("pip install colorama")
print("now you can run program :) ")
