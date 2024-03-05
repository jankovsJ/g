def main():
    soucet = 0

    while True:
        cislo = int(input("Zadeje číslo (0 pro final): "))
        if cislo == 0:
            break
        soucet += cislo

    print("Součet:", soucet)

if __name__ == "__main__":

    main()