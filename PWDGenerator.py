# learn generating passwords.
from random import randint

"""# generate random alphabets of length 8 in uppercase
password = ""
for pwd in range(8):
    pwd = chr(randint(65,90))
    print(pwd)
    password = password + pwd
print(password)"""

# generate random password of length 10
# first alphabet uppercase, second number followed by a special character.
# later 4 alphabets in lowercase and
# last alphabet uppercase followed by number followed by special character
password = ""
lowercount=0
for pwd in range(2):
    pwd = chr(randint(65,90))
    password = password + pwd
    pwd =chr(randint(49,57))
    password = password + pwd
    pwd = chr(randint(35, 36))
    password = password + pwd
    while lowercount<4:
          pwd = chr(randint(65,90)).lower()
          password = password + pwd
          lowercount = lowercount + 1
          if lowercount == 4:
             break
print(password)



