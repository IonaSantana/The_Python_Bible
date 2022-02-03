know_users = ["Barbara", "Emma", "Bob", "Joao", "Fred", "Renata"]

while True:
    print("Hi! My name is Travis")
    name = input("What is yout name? ").strip().capitalize()

    if name in know_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?").strip().lower()

        #apenas remove a primeira ocorrencia
        if remove == "y":
            know_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you leave anyway!")
        #se eu souber onde está a ocorrencia posso usar del L[pos].    
    
    else:
        print("Hmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)? ").strip().lower()

        if add_me == "y":
            know_users.append(name) #A = A + [name], A = A + list('BCD') / separa em B, C e D
        elif remove == "n":
            print("No worries, see you around!")


