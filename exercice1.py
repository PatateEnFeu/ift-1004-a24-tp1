import random  # Importation du module random pour générer des nombres aléatoires

# Génère un nombre entier aléatoire compris entre 10 et 100 inclus
# nombre_genere = random.randint(10, 100)

# Affiche le nombre entier aléatoire généré avec un message explicatif
# print(f"Le nombre aléatoire généré est : {nombre_genere}")


print("#########################################")
print("          IFT-1004 Airlines              ")
print("#########################################")
print("\nLa meilleure compagnie aérienne du monde !")

nbr_passagers = int(input('\nCombien de billets souhaitez-vous réserver: '))
num_passager = 1

prix_billet1 = 0
prix_billet2 = 0
prix_billet3 = 0
prix_global = 0

choix = 0

while choix != 2:
    while (nbr_passagers >= num_passager):
        print("\n===============")
        print(f'Passager {num_passager}/{nbr_passagers}')
        print("===============")

        print(f'Nom du passager {num_passager}: ',end="")
        nom = str(input(""))

        print(f'Âge du passager {num_passager}: ',end="")
        age = int(input(""))

        rabais = 0
        if age <= 3 :
            rabais = 0
            prix_billet = 0
            prix_billet1 += prix_billet
            print(f'\nPrix du billet réservé pour {nom}: {prix_billet:.2f}$')
            num_passager += 1

        elif age >= 65 :
            rabais = random.randint(15, 55)
            prix_billet = 150 - (150 * (rabais/100))
            prix_billet2 += prix_billet
            print(f'Rabais appliqué pour {nom}: {rabais}%')
            print(f'\nPrix du billet réservé pour {nom}: {prix_billet:.2f}$')
            num_passager += 1
        else:
            prix_billet = 150
            prix_billet3 += prix_billet
            print(f'\nPrix du billet réservé pour {nom}: {prix_billet:.2f}$')
            num_passager += 1
    
    if nbr_passagers != 0 :
        prix_global += prix_billet1 + prix_billet2 + prix_billet3 #Valeur à ne pas réinitialiser pour le prix cumulé
        prix_total = prix_billet1 + prix_billet2 + prix_billet3 #Valeurs qui seront réinitialiser à la fin de la boucle
        print (f"\nLe montant total à encaisser pour cette réservation est: {prix_total:.2f}$")

    print(f'\n1. Enregistrer un autre client')
    print(f'2. Quitter')
    print(f'Entrez votre choix: ', end="")
    choix = int(input(''))

    while choix != 1 and choix != 2 :
        print(f'Choix invalide, veuillez entrer 1 ou 2: ',end="")
        choix = int(input(''))       

# Réinitialisation des valeurs quand l'utilisateur fait le choix 1
    while choix == 1 :
        nbr_passagers = int(input('\nCombien de billets souhaitez-vous réserver: ')) # se répète quand la valeur entrée est 0
        num_passager = 1
        prix_billet1 = 0 
        prix_billet2 = 0 
        prix_billet3 = 0 
        prix_total = 0
        choix = 0
#Fin code quand l'utilisateur fait le choix 2 en affichant le montant total cumulè
    if choix == 2 :
        print(f'\nMontant total cumulé pour tous les clients enregistrés : {prix_global:.2f}$')
        print(f'Bye bye!')
