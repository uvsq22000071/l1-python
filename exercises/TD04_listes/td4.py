liste = [3, 5, 10]
liste.extend([2, 17])
liste[2] = -7
liste = [i * 2 for i in liste]
liste = [i + 1 for i in liste]
print(liste)