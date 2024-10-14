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

# fixed input
user_with_passwd = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# login
user = input("username: ")
passwd = input("password: ")

if user not in user_with_passwd or user_with_passwd[user] != passwd:
    print("unregistered user, terminating the program..")
    exit()
else:
    print(f"""
----------------------------------------
Welcome to the app, {user}
We have 3 texts to be analyzed.
----------------------------------------
""")   

#text analyse
choice_text_nr = int(input("Enter a number btw 1 and 3 to select: ")) 
print("----------------------------------------")

if 1 <= choice_text_nr <= 3:
    selected_text = TEXTS[choice_text_nr - 1]

    words = selected_text.replace(",", " ").split()
    
    count_words = len(words)  # 1
    count_titled = sum(1 for word in words if word.istitle())  # 2
    count_upper = sum(1 for word in words if word.isupper() and word.isalpha())  # 3
    count_lower = sum(1 for word in words if word.islower())  # 4
    count_numer_string = sum(1 for word in words if word.isdigit())  # 5
    sum_of_numbers = sum(int(word) for word in words if word.isdigit())  # 6

    print(f"There are {count_words} words in the selected text.")  # 1
    print(f"There are {count_titled} titlecase words.")  # 2
    print(f"There are {count_upper} uppercase words.")  # 3
    print(f"There are {count_lower} lowercase words.")  # 4
    print(f"There are {count_numer_string} numeric strings.")  # 5
    print(f"The sum of all the numbers is {sum_of_numbers}.")  # 6

print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")

length_occurrences = {}

words = selected_text.replace(",", "").split()

for word in words:
    length = len(word) 
    if length in length_occurrences:
        length_occurrences[length] += 1 
    else:
        length_occurrences[length] = 1  

for length in range(1, max(length_occurrences.keys()) + 1):
    occurrences = length_occurrences.get(length, 0)  
    print(f"{length:<2} | {'*' * occurrences:<12} | {occurrences}")

print("----------------------------------------")