import random  # Importation du module random pour générer des nombres aléatoires

# Génère un nombre entier aléatoire compris entre 10 et 100 inclus
# nombre_genere = random.randint(10, 100)

# Affiche le nombre entier aléatoire généré avec un message explicatif
# print(f"Le nombre aléatoire généré est : {nombre_genere}")


print("#########################################")
print("          IFT-1004 Airlines              ")
print("#########################################")
print("")
print("La meilleure compagnie aérienne du monde !")
print("")

nbr_passagers = int(input('Combien de billets souhaitez-vous réserver: '))
num_passager = 1

while (nbr_passagers >= num_passager):
        print("===============")
        print("Passager",num_passager,"/",nbr_passagers,)
        print("===============")

        print("Nom du passager",num_passager,": ", end="")
        nom = str(input(""))

        print("Âge du passager",num_passager,": ", end="")
        age = int(input(""))

        rabais = 0
        if age <= 3 :
            rabais = 0
            prix_billet = 0
            print("Prix du billet réservé pour",nom,": ",prix_billet,"$" )
        elif age >= 65 :
            rabais = random.randint(15, 55)
            prix_billet = 150 - (150 * (rabais/100))
            print("Rabais appliqué pour",nom,": ",rabais,"%")
            print("Prix du billet réservé pour",nom,": ",prix_billet,"$" )
        else:
            prix_billet = 150
            print("Prix du billet réservé pour",nom,": ",prix_billet,"$" )

    # elif : servira à gérer le cas ou le passager entre 0 dès le début

    