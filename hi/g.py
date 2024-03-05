def main():
    spravne_heslo = "GAAAAR"

    while True:
        zadane_heslo = input("Zadejte heslo: ")
        if zadane_heslo == spravne_heslo:
            print("Správné heslo. Přístup povolen.")
            break
        else:
            print("Nesprávné heslo. Zkuste to znovu.")

if __name__ == "__main__":
    
     main()