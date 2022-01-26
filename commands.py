# import os
# os.startfile("C:\SAPConsoleUtils\saplogon.exe")
# os.startfile(("C:\SAPConsoleUtils\putty.exe"))
# os.startfile("C:\SAPConsoleUtils\/rdp.exe")

import random
sat_numbers = []
number = 0

def is_there(number):
    if number not in sat_numbers:
        sat_numbers.append(number)


while len(sat_numbers) <= 5:
    number = random.randint(1, 59)

sat_numbers.sort()
sat_numbers.list()
print(sat_numbers)
