while True: 
    print(f"""
    1 - Řekni ahoj
    2 - Řekni vtip
    3 - Ukonči aplikaci""")

    choice = input("Zadej číslo volby: ")
    if choice.isdigit():
        choice = int(choise) 
    
    print ("Ahoj Jakube") if choice == 1 else None
    print ("Vtip: haha") if choice == 2 else None
    if choice == 3:
        print ("Ukončuji aplikaci...")
        break
    else:
        print ("Neplatná volba, zkus to znovu.")
        
        
		
