Zboží = ["CPU", "GPU", "RAM", "Motherboard", "Zdroj", "Case"]
Košík = []

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f" {x+1}: {prvek[x]}")
        print(" ")

vypis_pole(Zboží)

# Uživatel zvolí položku ze seznamu zboží, kterou chce přidat do košíku
index_vyber = int(input("Zadejte číslo zboží, které chcete přidat do košíku: ")) - 1

# Zkontrolujeme, zda je zadaný index platný
if 0 <= index_vyber < len(Zboží):
    prvek_vyber = Zboží[index_vyber]

    # Přidáme vybraný prvek do košíku
    Košík.append(prvek_vyber)

    # Odebere vybraný prvek ze seznamu zboží
    Zboží.pop(index_vyber)

    print("Položka byla úspěšně přidána do košíku.")
else:
    print("Zadaný index není platný.")

# Vypíšeme obsah košíku
print("Obsah košíku:")
vypis_pole(Košík)
