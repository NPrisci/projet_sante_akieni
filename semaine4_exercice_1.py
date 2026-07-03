# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 4 — Exercice 1 : Surveillance Epidémique Mpox
# Notions S4 : Boucles for, listes, accumulation
# Contexte : SITREP N°40 — Congo-Brazzaville 2025
# Priscillia NOUDOFININ
# ============================================================

print("=== Surveillance Epidémique Mpox — Congo-Brazzaville 2025 ===")
print()

#----Donnees des 9 districts sanitaires ----
# Format : [nom, departement, suspects, confirmes, deces]

districts = [
    ["Mossaka-Loukolela", "Cuvette", 12, 12, 0],
    ["Owando","Cuvette", 3, 2, 0],
    ["Oyo-Alima", "Cuvette", 3, 3, 0],
    ["Enyelle-Betou","Likouala", 1, 1, 0],
    ["Gamboma","Plateaux", 2, 2, 0],
    ["Lumumba","Pointe-Noire", 1, 1, 0],
    ["Mvou-mvou","Pointe-Noire", 1, 1, 0],
    ["Poto-Poto","Brazzaville", 1, 1, 0],
]

# ----Variables pour les totaux nationaux ----
total_suspects = 0
total_confirmes = 0
total_deces = 0
total_actifs = 0

# ----Compteurs par niveau d'alerte ----
zones_vertes = 0
zones_jaunes = 0
zones_oranges = 0
zones_rouges = 0

# ----Boucle principale: pacourir chaque district-----
for i, districts in enumerate(districts, 1):
    #Extraire les données du district
    nom = districts[0]
    departement = districts[1]
    suspects = districts[2]
    confirmes = districts[3]
    deces = districts[4]
    
    #calcul des indicateurs
    cas_actifs = confirmes - deces
    letalite = (deces / confirmes) * 100 if confirmes > 0 else 0

    #Determination du niveau d'alerte
    if confirmes >= 10:
        alerte = "Rouge"
        zones_rouges += 1
    elif 5 <= confirmes <= 9:
        alerte = "Orange"
        zones_oranges += 1
    elif 2 <= confirmes <= 4:
        alerte = "Jaune"
        zones_jaunes += 1
    else:
        alerte = "Verte"
        zones_vertes += 1
    
    #Accumulation des totauxs nationaux
    total_suspects += suspects
    total_confirmes += confirmes
    # total_confirmes = total_confirmes + confirmes
    total_deces += deces
    total_actifs += cas_actifs

    #Affichage du district
    print(f"-----District {i} -----")
    print(f"Nom du district: {nom}")
    # print(f"Département: {departement}")
    print(f"Cas suspects: {suspects}")
    print(f"Cas confirmés: {confirmes}")
    print(f"Décès: {deces}")
    print(f"Cas actifs: {cas_actifs}")
    print(f"Létalité: {letalite:.2f}%")
    print(f"Niveau d'alerte: {alerte}")
    print()

# ----Rapport national ----
print("===========================================================")
print("=== Rapport National MPOX 2025 ===")
print("===========================================================")
print(f"Districts analysés: {len(districts)}")
print(f"Cas suspects nationaux: {total_suspects}")
print(f"Cas confirmés nationaux: {total_confirmes}")
print(f"Décès nationaux: {total_deces}")
print(f"Cas actifs nationaux: {total_actifs}")
print()
print(f"Zones vertes: {zones_vertes}")
print(f"Zones jaunes: {zones_jaunes}")
print(f"Zones oranges: {zones_oranges}")
print(f"Zones rouges: {zones_rouges}")
print("===========================================================")