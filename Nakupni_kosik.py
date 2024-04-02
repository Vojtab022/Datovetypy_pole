Zboží = ["CPU", "GPU", "RAM", "Motherboard", "Zdroj", "Case"]
Košík = []


def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f" {x+1}: {prvek[x]}")
        print(" ")

vypis_pole(Zboží)

prvek_vyber = int(input("Zadejte číslo zboží, které chcete přidat do košíku: ")) - 1

prvek_vyber2 = Zboží[prvek_vyber]

Košík.append(prvek_vyber2)

Zboží.pop(prvek_vyber)

print("Obsah košíku:")
vypis_pole(Košík)

print("--------------------")
vypis_pole(Zboží)