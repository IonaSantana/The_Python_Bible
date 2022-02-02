name = input('Qual seu nome? ')
age = input('E sua idade? ')
city = input('E você mora em qual cidade? ')
enjoy = input('E o que você gosta de fazer no seu tempo livre? ')

exit = "{}, {}, {}, {}".format(name, age, city, enjoy)

print(exit, '\n\n')

exit = "Seu nome: {1}\nSua idade:{0}\nOnde você mora: {2}\nO que você ama fazer: {3}".format(age, name, city, enjoy)

print(exit)