def syracuse(n):
    liste = [n]
    while list[-1] != 1:
        if list[-1] % 2 == 0:
            liste.append(liste[-1] // 2)
        else:
            liste.append(liste[-1] * 3 + 1)
    return liste
print(syracuse(3))

def tempsVol(n):
    """ Retourne le temps de vol de n """
    liste = syracuse(n)
    temps_de_vol = len(liste) - 1
    return temps_de_vol

print("Le temps de vol de", 3, "est", tempsVol(3))