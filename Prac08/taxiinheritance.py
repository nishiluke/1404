from Prac08.taxi import Taxi

def main():
    taxis = []
    taxis.append(Taxi("Limo", 100))
    taxis.append(Taxi("Prius", 100))
    taxis.append(Taxi("Hummer", 200))
    totalCost = 0
    driveCost = 0
    print("Lets drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        menuChoice = str(input(">>> "))
        if menuChoice == "q":
            break

        elif menuChoice == "c":
            print("Taxis available:")
            i = 0
            for taxi in taxis:
                print("{} - {}".format(i,taxi))
                i += 1
            taxiChoice = int(input("Choose taxi: "))
            while taxiChoice < 0 or taxiChoice > len(taxis) - 1:
                print("Invalid number")
                taxiChoice = int(input("Choose taxi: "))

        elif menuChoice == "d":
            driveDistance = int(input("Drive how far?: "))
            taxis[taxiChoice].start_fare()
            taxis[taxiChoice].drive(driveDistance)
            driveCost = taxis[taxiChoice].get_fare()
            print("That trip cost you ${:.2f}".format(driveCost))
        else:
            print("invalid option")

        totalCost += driveCost
        driveCost = 0
        print("Bill to date: ${:.2f}".format(totalCost))
main()