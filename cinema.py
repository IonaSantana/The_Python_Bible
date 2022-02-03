from random import choice


films = {
    "Finding Dory": {"Classification": 3, "Seat": 5},
    "Bourne": {"Classification": 18, "Seat": 5},
    "Tarzan": {"Classification": "free", "Seat": 3},
    "Ghost Busters": {"Classification": 12, "Seat": 2}
}

while True:
    choice = input("What film would you like to watch? ").strip().title()

    if choice in films:
        age = int(input("How old are you? ").strip())

        classification = films[choice]["Classification"];
        if classification == 'free' or age >= classification:
            num_seats = films[choice]["Seat"]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice]["Seat"] = num_seats - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film")
    else:
        print("We don't have that film")