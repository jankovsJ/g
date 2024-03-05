def main():
    cislo_mesice = int(input("Zadejte číslo měsíce: "))

    mesice = {
        1: "leden",
        2: "únor",
        3: "březen",
        4: "duben",
        5: "květen",
        6: "červen",
        7: "červenec",
        8: "srpen",
        9: "září",
        10: "říjen",
        11: "listopad",
        12: "prosinec"
    }

    if cislo_mesice in mesice:
        print("Název měsíce:", mesice[cislo_mesice])
    else:
        print("Chybné číslo měsíce.")

if __name__ == "__main__":
    main()
