"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Vaško
email: t.vasko@seznam.cz
discord: tvasko007
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
] 

import os

user_data = {"bob" : "123","ann" : "pass123","mike" : "password123",
             "liz" : "pass123"}
separator = "=" * 40

while True:
    if user_name := input("ENTER YOUR NAME: "):
        break
    print("EMPTY INPUT. TRY AGAIN....")

while True:   
    if password := input("ENTER YOUR PASSWORD: "):
        break
    print("EMPTY INPUT. TRY AGAIN...")
    
print(separator)

if password == str(user_data.get(user_name)):
    print(f"WELCOME TO THE APP, {user_name.upper()}!")
    print(f"WE HAVE {len(TEXTS)} TEXTS TO BE ANALYZED.")    
    
    print(separator)
    
else:
    os.system("cls")
    print("UNREGISTERED USER, TERMINATING THE PROGRAM..")
    exit()
         
while True:   
    choice = input(f"ENTER A NUMBER BTW. 1 AND {len(TEXTS)} TO SELECT:\n")

    print(separator)

    if not choice.isnumeric() or int(choice) not in range(1, len(TEXTS) + 1):
        os.system("cls") 
        print("INVALID INPUT. CHOOSE ONLY NUMBERS BETWEEN 1-3")
        exit()
            
    else:
        choice = TEXTS[int(choice) - 1]
        break

splited_text = choice.split()
words = [word.strip(",.?!") for word in splited_text]
numbers_of_length = [len(word) for word in words]
title_case = [word for word in words if word.istitle()]
all_upper = [word for word in words if word.isupper() and word.isalpha()]
all_lower = [word for word in words if word.islower()]
numeric_string = [word for word in words if word.isnumeric()]
numeric_int = [int(number) for number in numeric_string]

print(f"THERE ARE {len(numbers_of_length)} WORDS IN SELECTED TEXT.")
print(f"THERE ARE {len(title_case)} TITLECASE WORDS.")
print(f"THERE ARE {len(all_upper)} UPPERCASE WORDS.")
print(f"THERE ARE {len(all_lower)} LOWERCASE WORDS.")
print(f"THERE ARE {len(numeric_string)} NUMERIC STRINGS.")
print(f"THE SUM OF ALL THE NUMBERS IS {sum(numeric_int)}.")
print(separator)
print("LEN| OCCURENCES| NR.")
print(separator)

star = "*"
space = " "
set_numbers = set(numbers_of_length)
frequency = []

for each in set_numbers:
    frequency.append(numbers_of_length.count(each))
highest_number = max(frequency)

for num in set_numbers:
    count_of_spaces = highest_number - numbers_of_length.count(num)
    print(
        f"{num:2d} | {star * numbers_of_length.count(num)}"
        f"{space * count_of_spaces} | {numbers_of_length.count(num)}"
    )
