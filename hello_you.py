name = input('Qual seu nome? ')
age = input('E sua idade? ')
city = input('E você mora em qual cidade? ')
enjoy = input('E o que você gosta de fazer no seu tempo livre? ')

exit = "{}, {}, {}, {}".format(name, age, city, enjoy)

print(exit)

exit = "{1}, {0}, {2}, {3}".format(age, name, city, enjoy)

print(exit)