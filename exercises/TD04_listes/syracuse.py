def syracuse(n):
    res = []
    while True:
        res.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return res
print(syracuse(3))

def testeConjecture(n_max):
    for i in range(1, n_max + 1):
        syracuse(i)
    return True
print(testeConjecture(10000))

def tempsVol(n):
    cpt = 0
    while True:
        if n == 1:
            break
        cpt += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return cpt
print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    return [tempsVol(i) for i in range(1, n_max + 1)]
print(tempsVolListe(100))

liste_vol = tempsVolListe(10000)
vol_max = max(liste_vol)
print("temps de vol maximum:", vol_max)
print("atteint par l'entier", liste_vol.index(vol_max) + 1)

def alt_max(n):
    alt = n
    while True:
        if n == 1:
            break
        if n > alt:
            alt = n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return alt
print("L'altitude maximale de 3 est", alt_max(3))
liste_altitude = [alt_max(i) for i in range(1, 10001)]
altitude_max = max(liste_altitude)
print("L'altitude maxiamle entre 1 et 10000 est", altitude_max)
print("elle est atteinte par l'entier", liste_altitude.index(altitude_max) + 1)