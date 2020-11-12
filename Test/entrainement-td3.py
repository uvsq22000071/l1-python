def tempsEnSeconde(temps):
    return(((temps[0] * 24) + temps[1]) * 60 + temps[2]) * 60 + temps[3]
temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    minute = seconde // 60
    seconde %= 60
    heure = minute // 60
    minute %= 60
    jour = heure // 24
    heure %= 24
    return(jour, heure, minute, seconde)
temps = secondeEnTemps(100000)
print(temps[0], temps[1], temps[2], temps[3])

def affichePLuriel(val,mot):
    if val != 0:
        print("",val,mot,end="")
    if val > 1:
        print("s",end="")
def afficheTemps(temps):
    affichePLuriel(temps[0],"jour")
    affichePLuriel(temps[1],"heure")
    affichePLuriel(temps[2],"minute")
    affichePLuriel(temps[3],"seconde")
    print("")
afficheTemps((1, 0, 54, 2))

def demandeTemps():
    jour = int(input("Combien de jours ?"))
    heure = int(input("Combien d'heures ?"))
    minute = int(input("Combien de minutes ?"))
    seconde = int(input("Combien de secondes ?"))
    if (seconde > 59 or minute > 59 or heure > 23):
        print("Entrée mal formée, veuillez rentrer de nouvelles informations")
        return(0,0,0,0)
    return(jour, heure, minute, seconde)
afficheTemps(demandeTemps())

def sommeTemps(temps1, temps2):
    temps1 = tempsEnSeconde(temps1)
    temps2 = tempsEnSeconde(temps2)
    temps3 = temps1 + temps2
    temps3 = secondeEnTemps(temps3)
    return(temps3)
sommeTemps((2,3,4,25),(5,22,57,1))