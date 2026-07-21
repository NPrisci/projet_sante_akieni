taches = []

def menu():
    print("TO DO LIST")
    print("1. Ajouter une tache à faire")
    print("2. Afficher les taches")
    print("3. Modifier une tache ")
    print("4. Marquer une tache comme terminée")
    print("5. Supprimer une tache")
    print("6. Quitter")

def ajout_tache():
    titre = input("Entrez le titre de la tache : ")
    tache = {
        "titre": titre, 
        "terminée": False 
    }
    taches.append(tache)
    print("Tache ajoutée avec succès")  

def afficher_tache():
    if len(taches) == 0:
        print("Aucune tache enregistrée.")
        return
    print("Liste des taches à faire")
    for i, tache in enumerate(taches, 1):
        if tache["terminée"]:
            etat = "✓"  #  symbole pour terminé
        else:
            etat = "○"  # symbole pour non terminé
        print(f"{i}. {etat} {tache['titre']}")

def modifier_tache():
    afficher_tache()
    if len(taches) == 0:
        return
    num = int(input("Numero de la tache à modifier : "))
    if 1 <= num <= len(taches):
        nouveau = input("Nouveau titre : ")
        taches[num - 1]["titre"] = nouveau
        print("Tache modifiée")
    else:
        print("Numéro invalide.")

def terminer_tache():
    afficher_tache()
    if len(taches) == 0:
        return
    numero = int(input("Numéro de la tache terminée : "))
    if 1 <= numero <= len(taches):
        taches[numero - 1]["terminée"] = True 
        print("Tache marquée comme terminée")
    else:
        print("Numéro invalide.") 

def supprimer_tache():
    afficher_tache()
    if len(taches) == 0:
        return
    num = int(input("Numéro de la tache à supprimer: "))
    if 1 <= num <= len(taches):
        taches.pop(num - 1)
        print("Tache supprimée.")
    else:
        print("Numéro invalide.")

while True:
    menu()
    
    choix = input("Entrez le nombre de l'action que vous souhaitez executer: ")  
    if choix == "1":
        ajout_tache()
    elif choix == "2":
        afficher_tache()
    elif choix == "3":
        modifier_tache()
    elif choix == "4":
        terminer_tache()
    elif choix == "5":
        supprimer_tache()
    elif choix == "6":
        print("Merci d'avoir utilisé mon app")
        break  
    else:
        print("Choix invalide.")