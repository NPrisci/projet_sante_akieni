# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 4 — Exercice 1 : Surveillance Epidémique Mpox
# Notions S4 : Boucles for, listes, accumulation
# Contexte : SITREP N°40 — Congo-Brazzaville 2025
# Priscillia NOUDOFININ
# ============================================================

print("=== Surveillance Epidémique Mpox — Congo-Brazzaville 2025 ===")
print()

#Initialisation des données de la liste districts(liste vide)
districts = []

#L'utilisateur entre le nombre de districts sanitaires à analyser
nb_districts = int(input("Entrez le nombre de districts sanitaires à analyser : "))
for i in range (1, nb_districts+1):
    print("District ",i," :")
    nom = input("Nom du district : ")
    departement = input("Departement : ")
    suspects = int(input("Cas suspects : "))
    confirmes = int(input("Cas confirmes : "))
    deces = int(input("Deces : "))

    #j'atoute les données du district i dans la liste districts
    districts.append([nom,departement,suspects,confirmes,deces])

# variables pour les totaux nationaux

total_suspects  = 0
total_confirmes = 0
total_deces     = 0
total_actifs    = 0

# variables pour les compteurs par niveau d'alerte
zones_vertes    = 0
zones_jaunes    = 0
zones_oranges   = 0
zones_rouges    = 0
# nb_districts    = 9

for i in range(nb_districts):
    print('--- District', i, '---')
    nom_district = districts[i][0]
    departement  = districts[i][1]
    suspects     = districts[i][2]
    confirmes    = districts[i][3]
    deces        = districts[i][4]
    cas_actifs = confirmes - deces                    # TODO 1
    # Calcul de la letalite
    if confirmes > 0:
        letalite = (deces / confirmes) * 100              # TODO 2
    else:
        letalite = 0
    # Determination du niveau d'alerte
    if confirmes >= 10:
        alerte = 'ROUGE'
        zones_rouges = zones_rouges + 1                  # TODO 3
    elif confirmes >= 5:
        alerte = 'ORANGE'
        zones_oranges = zones_oranges + 1                 # TODO 4
    elif confirmes >= 2:
        alerte = 'JAUNE'
        zones_jaunes = zones_jaunes + 1                  # TODO 5
    else:
        alerte = 'VERT'
        zones_vertes = zones_vertes + 1
    total_suspects  = total_suspects  + suspects
    total_confirmes = total_confirmes + confirmes                   # TODO 6
    total_deces     = total_deces     + deces                   # TODO 7
    total_actifs    = total_actifs    + cas_actifs                   # TODO 8
    print('  Alerte   :', alerte)
    print('  Actifs   :', cas_actifs)
    print('  Letalite :', round(letalite, 1), '%')
    print()
print('=======================================')
print('      RAPPORT NATIONAL MPOX 2025       ')
print('=======================================')
print('Districts analyses   :', nb_districts)
print('Total suspects       :', total_suspects)
print('Total confirmes      :', total_confirmes)
print('Total deces          :', total_deces)
print('Total cas actifs     :', total_actifs)
print('Zones VERTES         :', zones_vertes)
print('Zones JAUNES         :', zones_jaunes)
print('Zones ORANGES        :', zones_oranges)
print('Zones ROUGES         :', zones_rouges)
print('=======================================')