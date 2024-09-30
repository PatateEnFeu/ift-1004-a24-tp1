hauteur = int(input(f"Entrez la hauteur: "))
lignes = hauteur + 1

if hauteur < 4 :
   print(f"Hauteur incorrecte")

elif hauteur > 4 :
    for i in range(1, hauteur+1):
        print(' ' * (hauteur - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
