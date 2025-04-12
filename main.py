TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
line=(40*"-") #grafický oddělovač jednotlivých textů

users = dict(
    {"bob": "123",
     "ann": "pass123",
     "mike": "password123",
     "liz": "pass123"}) #uživatelské jména a hesla

def identifikace(user:str,password:str) -> bool: # porovnává jméno a heslo s knihovnou 
    if users.get(user) == password:
        return True
    else: return False

def exist(status:bool) ->str: # vrací text podle úspěšnosti identifikace
    if status:
        return(f"""{line}\nWelcome to the app, {user}
We have {sum_texts} texts to be analyzed.
{line}""")
       
    else:
        exit(f"""unregistered user, terminating the program...""") 

def preparing(text:str) -> list: # vymaže interpunkci a rozseká text na jednotlivá slova
    stripped = text.replace(".","").replace("-", "").replace(",", "").replace("!", "").replace("?", "").replace("\n", "").replace("  ", " ")
    cutting = stripped.split()
    return(cutting)

def words_count(list) -> int: # počítá slova v textu
    return len(words)

def title_case(list) -> int:  # počítá slova začínající velkým písmenem
    is_title_count = 0
    for i in words:
        if i.istitle():
            is_title_count += 1
    return is_title_count

def upper_case(list) -> int:  # počítá slova psaná kapitálkami
    is_upper_count = 0
    for i in words:
        if i.isupper():
            is_upper_count += 1
    return is_upper_count

def lower_case(list) -> int:  # počítá slova psaná maluskami
    is_lower_count = 0
    for i in words:
        if i.islower():
            is_lower_count += 1
    return is_lower_count

def digit_case(list) -> int:  # počítá slova z čísel
    is_digit_count = 0
    for i in words:
        if i.isdigit():
            is_digit_count += 1
    return is_digit_count

def sum_digits(list) -> int:  # sčítá čísla v textu
    total_sum= 0
    for i in words:
        if i.isdigit():
            total_sum+= int(i)
    return sum

def statistics (list) -> (dict): # počítá délku jednotlivých slov a jejich výskyt, dict řadí podle délky slov
    stat_container = dict()

    for i in words:
        if len(i) in stat_container:
            stat_container [len(i)] += 1
        else:
            stat_container [len(i)] = 1
    stat_sorted = dict(sorted(stat_container.items()))
    return (stat_sorted)

sum_texts = len(TEXTS) # vrací počet textů v knihovně

user = input("Zadejte uživatelské jméno: ")
password = input("Zadejte heslo: ")

status = bool(identifikace(user,password)) # vrací výsledek identifikace uživalete

print(f"""username:{user}\npassword:{password}\n{exist(status)}""")

while True:         # Ošetřený vstupu výběru textu
    try:
        choosed_text = int(input("Enter a number btw. 1 and 3 to select: "))
        if 0 < choosed_text < 4:
            break 
        else:
            print("Maybe I misunderstood you. Enter a number btw. 1 and 3 to select: ") 
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

words = preparing(TEXTS[choosed_text-1]) # základní kámen pro další operace
sorted_stats = statistics(words)    # volá funkci pro statistiku zastoupení délky jednotlivých slov

print(f"""There are {words_count(words)} words in the selected text. 
There are {title_case(words)} titlecase words.
There are {upper_case(words)} uppercase words.
There are {lower_case(words)} lowercase words.
There are {digit_case(words)} numeric strings.
The sum of all the numbers {sum_digits(words)}
{line}
LEN|{5*" "}OCCURENCES{5*" "}|NR.
{line}""")

for i in sorted_stats:  # vypíše statistiku do tabulky
    print(f"{("  ") if i<10 else (" ")}{i}|{sorted_stats[i]*"*"}{(20-sorted_stats[i])*" "}|{sorted_stats[i]}", end="\n")
print(line)

input() # čeká na stisk enteru pro ukončení programu
