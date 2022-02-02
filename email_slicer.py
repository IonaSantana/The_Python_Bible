email = input("Qual é o seu email: ").strip(" ")

username = email[0:email.find('@') : 1]

domain = email[email.index('@') + 1 : ]

output = "Seu nome de usuário: {}\nO dominío: {}".format(username,domain)

print(output)