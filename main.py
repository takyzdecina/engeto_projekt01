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

line = (40*"-") # grafický oddělovač jednotlivých textů

users = { # uživatelské jména a hesla
	"bob": "123",
	"ann": "pass123",
	"mike": "password123",
	"liz": "pass123"} 

def identifikace(user:str,password:str) -> bool: # porovnává jméno a heslo s knihovnou 
	return users.get(user) == password

def preparing(text:str) -> list: # vymaže interpunkci a rozseká text na jednotlivá slova
	stripped = (text.replace(".","") # maže daný interpunkční znak
			 .replace("-", "")  # maže daný interpunkční znak
			 .replace(",", "")  # maže daný interpunkční znak
			 .replace("!", "")  # maže daný interpunkční znak
			 .replace("?", "")  # maže daný interpunkční znak
			 .replace("\n", "") # maže daný interpunkční znak
			 .replace("  ", " "))   # maže dvě mezery
	cutting = stripped.split()  # rozděluje text na jednotlivá slova
	return(cutting)

from typing import NamedTuple,Dict,List # importuje potřebné knihovny pro práci s daty

class letters_stat(NamedTuple): # vytvoří NamedTuple pro statistiku
	words_sum: int
	title_case: int
	upper_case: int
	lower_case: int
	digit_case: int
	sum_digits: int

def all_counting(buffer_words:List[str]) -> letters_stat: # počítá zastoupení jednotlivých slov
    is_another_word = 0 # všechna slova
    is_title_count = 0  # slova s velkým písmenem
    is_upper_count = 0  # slova psaná velkými písmeny
    is_lower_count = 0  # slova psaná malými písmeny
    is_digit_count = 0  # čísla v textu
    is_digit_sum = 0    # součet čísel v textu
    
    for word in buffer_words:   # pracuje se slovy
        is_title_count += 1 if word.istitle() else 0    # počítá slova začínající velkým písmenem
        is_upper_count += 1 if word.isupper() else 0    # počítá slova psaná velkými písmeny
        is_lower_count += 1 if word.islower() else 0    # počítá slova psaná malými písmeny
        is_another_word += 1                             # počítá celkový počet slov

        if word.isdigit():  # pracuje s čísly
            is_digit_count += 1                         # počítá čísla v textu
            is_digit_sum += int(word)                      # počítá součet čísel v textu
        else: 0
    
    return letters_stat(
		words_sum = is_another_word,
		title_case = is_title_count,
		upper_case = is_upper_count,
		lower_case = is_lower_count,
		digit_case = is_digit_count,
		sum_digits = is_digit_sum)

def statistics (list) -> (dict): # počítá délku jednotlivých slov a jejich výskyt, dict řadí podle délky slov
	stat_container = dict() # vytvoří prázdný slovník pro statistiku

	for i in all_words:
		if len(i) in stat_container:    # pokud je délka slova už v dictionary, přičte 1
			stat_container [len(i)] += 1
		else:
			stat_container [len(i)] = 1 # jinak přidá do slovníku délku slova a nastaví počet na 1
	stat_sorted = dict(sorted(stat_container.items()))  # seřadí hodnoty podle klíče (délka slova) vzestupně
	return (stat_sorted)

sum_texts = len(TEXTS) # vrací počet textů v knihovně

# začátek hlavičky
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Šmíd
email: smidjakub13@gmail.com	
""")
# konec hlavičky

user = input("username:")
password = input("password:")

if identifikace(user,password):
	print(f"""{line}\nWelcome to the app, {user}
We have {sum_texts} texts to be analyzed.
{line}""")
else:
	exit(f"""unregistered user, terminating the program...""")

while True:		 # Ošetřený vstupu výběru textu
	try:
		choosed_text = int(input(f"Enter a number btw. 1 and {sum_texts} to select: "))
		if 0 < choosed_text < (sum_texts+1):
			break 
		else:
			print(f"Maybe I misunderstood you.", end = " ") 
	except ValueError:
		print(F"Maybe I misunderstood you.", end = " ")

all_words = preparing(TEXTS[choosed_text-1]) # list s jednotlivými slovy textu - základní kámen pro další operace
counting_output = all_counting(all_words) # volá funkci pro spočítání zastoupení jednotlivých slov
sorted_stats = statistics(all_words)	# volá funkci pro statistiku zastoupení délky jednotlivých slov

print(f"""There are {counting_output.words_sum} all_words in the selected text. 
There are {counting_output.title_case} titlecase all_words.
There are {counting_output.upper_case} uppercase all_words.
There are {counting_output.lower_case} lowercase all_words.
There are {counting_output.digit_case} numeric strings.
The sum of all the numbers {counting_output.sum_digits}
{line}
LEN|{5*" "}OCCURENCES{5*" "}|NR.
{line}""")

for i in sorted_stats:  # vypíše statistiku do tabulky
	print(f"{("  ") if i < 10 else (" ")}{i}|{sorted_stats[i]*"*"}{(20-sorted_stats[i])*" "}|{sorted_stats[i]}", end = "\n")
print(line)

input() # čeká na stisk enteru pro ukončení programu