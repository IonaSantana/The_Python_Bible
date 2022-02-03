from random import choice
question = ["Por que o seu é azul? ", 
            "Por que o queijo tem buracos? ", 
            "Por que a água é transparente? ", 
            "Onde estão os dinossauros? "]

question = choice(question)
answer = input(question).strip().lower()

while answer != "porque sim":
    answer = input("Por quê? ").strip()

print("Oh... Okay")