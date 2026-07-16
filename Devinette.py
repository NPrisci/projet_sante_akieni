import random


def choix_difficulte():
    print("========== DEVINE LE NOMBRE ==========")
    print("Choisis une difficulté :")
    print("1 - Facile (1 à 20)")
    print("2 - Moyen (1 à 50)")
    print("3 - Difficile (1 à 100)")

    choix = input("Ton choix : ")

    if choix == "1":
        return 20
    elif choix == "2":
        return 50
    else:
        return 100


def jeux(maxi):

    secret = random.randint(1, maxi)

    essais = 0
    propositions = []

    while True:

        propo = int(input(f"Entre un nombre entre 1 et {maxi} : "))

        propositions.append(propo)
        essais += 1

        if propo < secret:

            if secret - propo > 10:
                print("Votre nombre est trop petit.")
            else:
                print("Votre nombre est petit.")

        elif propo > secret:

            if propo - secret > 10:
                print("Votre nombre est trop grand.")
            else:
                print("Votre nombre est grand.")

        else:
            print("\n Félicitations ! Vous avez trouvé le nombre.")
            return essais, propositions


def score(essais, propositions):

    print("\n========== SCORE ==========")
    print(f"Vous avez gagné après {essais} essai(s).")

    print("\nVos propositions étaient :")
    print(propositions)


def rejouer():

    reponse = input("\nVoulez-vous rejouer ? (o/n) : ")

    return reponse.lower() == "o"


while True:

    maximum = choix_difficulte()

    essais, propositions = jeux(maximum)

    score(essais, propositions)

    if not rejouer():
        print("\nMerci d'avoir joué !")
        break