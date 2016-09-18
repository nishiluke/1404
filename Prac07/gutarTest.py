from Prac07.guitar import Guitar

def main():
    guitars = []
    i = 0
    while True:
        menu = str(input("Add a guitar?(y/n): ")).upper()
        if menu == "N":
            break
        elif menu == "Y":
            newName = str(input("Name: "))
            newYear = int(input("Year: "))
            newCost = float(input("Cost: "))
            guitars.append(Guitar(newName, newYear, newCost))
            print("{} added".format(guitars[i]))
            i += 1
        else:
            print("invalid input")

    print("My guitars:")
    i = 1
    for guitar in guitars:
        print("Guitar {}: {}".format(i, guitar))
        i += 1
main()