def nummer_liste(ting1: str, ting2: str, ting3: str, ting4: str, ting5: str) -> str:
    """
    Lager en nummer liste av de fem input-strengene.

    Argumenter:
        ting1: Første element.
        ting2: Andre element.
        ting3: Tredje element.
        ting4: Fjerde element.
        ting5: Femte element.

    Returns:
        str: En nummer-liste av input-elementene.
    """
    nummer_liste = f"1. {ting1}\n2. {ting2}\n3. {ting3}\n4. {ting4}\n5. {ting5}"
    return nummer_liste

print(nummer_liste("Torsk", "Hyse", "Sei", "Laks", "Makrell"))
print(nummer_liste("Rashford", "Messi", "Ronaldo", "Pogba", "Neymar"))
print(nummer_liste("Pizza", "Taco", "Hamburger", "Pølse", "Is"))