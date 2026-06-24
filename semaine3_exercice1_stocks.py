# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 1 : Classification Stocks Medicaments
# Utilise les notions de S2 (variables, types, operateurs, f-strings)
# + S3 (if/elif/else, conditions composees)
# ============================================================

# --- DONNEES S2 : Variables medicaments ---
# (Reimporter depuis sante_variables.py ou redeclarer ici)

# Medicament 1 - Artemether-Lumefantrine
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   # FCFA

# Medicament 2 - Amoxicilline 500mg
m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0

# Medicament 3 - Paracetamol 500mg
m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0

# Medicament 4 - SRO (sachets)
m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0

# Medicament 5 - Vaccin DTP-HepB-Hib
m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0

# --- CLASSIFICATION MEDICAMENT 1 : Artemether-Lumefantrine ---
# S3 (nouveau) : if / elif / else
# S2 (reutilise) : operateurs arithmetiques pour calcul des seuils

print("\n" + "="*65)
print("  CLASSIFICATION DES MEDICAMENTS")
print("="*65)

# Medicament 1
print("\n--- Medicament 1 ---")
if m1_stock <= m1_seuil_rupture:
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut  = 'ALERTE STOCK'
    m1_couleur = '[ORANGE]'
    m1_action  = 'Commande urgente a declencher sous 72h'
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut  = 'STOCK LIMITE'
    m1_couleur = '[JAUNE]'
    m1_action  = 'Surveillance renforcee — planifier commande'
else:
    m1_statut  = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action  = 'Situation normale — suivi standard'

print(f"  {m1_couleur} {m1_nom}")
print(f"      Stock : {m1_stock} unites | Seuil : {m1_seuil_rupture}")
print(f"      Seuil*1.5 : {m1_seuil_rupture * 1.5} | Seuil*2.0 : {m1_seuil_rupture * 2.0}")
print(f"      Statut : {m1_statut}")
print(f"      Action : {m1_action}")

# Medicament 2
print("\n--- Medicament 2 ---")
if m2_stock <= m2_seuil_rupture:
    m2_statut  = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut  = 'ALERTE STOCK'
    m2_couleur = '[ORANGE]'
    m2_action  = 'Commande urgente a declencher sous 72h'
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut  = 'STOCK LIMITE'
    m2_couleur = '[JAUNE]'
    m2_action  = 'Surveillance renforcee — planifier commande'
else:
    m2_statut  = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action  = 'Situation normale — suivi standard'

print(f"  {m2_couleur} {m2_nom}")
print(f"      Stock : {m2_stock} unites | Seuil : {m2_seuil_rupture}")
print(f"      Seuil*1.5 : {m2_seuil_rupture * 1.5} | Seuil*2.0 : {m2_seuil_rupture * 2.0}")
print(f"      Statut : {m2_statut}")
print(f"      Action : {m2_action}")

# Medicament 3
print("\n--- Medicament 3 ---")
if m3_stock <= m3_seuil_rupture:
    m3_statut  = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut  = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action  = 'Commande urgente a declencher sous 72h'
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut  = 'STOCK LIMITE'
    m3_couleur = '[JAUNE]'
    m3_action  = 'Surveillance renforcee — planifier commande'
else:
    m3_statut  = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action  = 'Situation normale — suivi standard'

print(f"  {m3_couleur} {m3_nom}")
print(f"      Stock : {m3_stock} unites | Seuil : {m3_seuil_rupture}")
print(f"      Seuil*1.5 : {m3_seuil_rupture * 1.5} | Seuil*2.0 : {m3_seuil_rupture * 2.0}")
print(f"      Statut : {m3_statut}")
print(f"      Action : {m3_action}")

# Medicament 4
print("\n--- Medicament 4 ---")
if m4_stock <= m4_seuil_rupture:
    m4_statut  = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut  = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action  = 'Commande urgente a declencher sous 72h'
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut  = 'STOCK LIMITE'
    m4_couleur = '[JAUNE]'
    m4_action  = 'Surveillance renforcee — planifier commande'
else:
    m4_statut  = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action  = 'Situation normale — suivi standard'

print(f"  {m4_couleur} {m4_nom}")
print(f"      Stock : {m4_stock} unites | Seuil : {m4_seuil_rupture}")
print(f"      Seuil*1.5 : {m4_seuil_rupture * 1.5} | Seuil*2.0 : {m4_seuil_rupture * 2.0}")
print(f"      Statut : {m4_statut}")
print(f"      Action : {m4_action}")

# Medicament 5
print("\n--- Medicament 5 ---")
if m5_stock <= m5_seuil_rupture:
    m5_statut  = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut  = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action  = 'Commande urgente a declencher sous 72h'
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut  = 'STOCK LIMITE'
    m5_couleur = '[JAUNE]'
    m5_action  = 'Surveillance renforcee — planifier commande'
else:
    m5_statut  = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action  = 'Situation normale — suivi standard'

print(f"  {m5_couleur} {m5_nom}")
print(f"      Stock : {m5_stock} unites | Seuil : {m5_seuil_rupture}")
print(f"      Seuil*1.5 : {m5_seuil_rupture * 1.5} | Seuil*2.0 : {m5_seuil_rupture * 2.0}")
print(f"      Statut : {m5_statut}")
print(f"      Action : {m5_action}")

# --- COMPTAGE DES ALERTES ---
# S2 (reutilise) : variables numeriques
# S3 (nouveau) : conditions pour compter

nb_ruptures_critiques = 0
nb_alertes_stock = 0
nb_stocks_normaux = 0

# Comptage des ruptures critiques
if m1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
if m2_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
if m3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
if m4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
if m5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1

# Comptage des alertes stock
if m1_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
if m2_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
if m3_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
if m4_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
if m5_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1

# Comptage des stocks normaux
if m1_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1
if m2_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1
if m3_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1
if m4_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1
if m5_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1

# Liste des medicaments en rupture pour l'alerte
medicaments_rupture = []
if m1_statut == 'RUPTURE CRITIQUE':
    medicaments_rupture.append(m1_nom)
if m2_statut == 'RUPTURE CRITIQUE':
    medicaments_rupture.append(m2_nom)
if m3_statut == 'RUPTURE CRITIQUE':
    medicaments_rupture.append(m3_nom)
if m4_statut == 'RUPTURE CRITIQUE':
    medicaments_rupture.append(m4_nom)
if m5_statut == 'RUPTURE CRITIQUE':
    medicaments_rupture.append(m5_nom)

# Liste des medicaments en alerte
medicaments_alerte = []
if m1_statut == 'ALERTE STOCK':
    medicaments_alerte.append(m1_nom)
if m2_statut == 'ALERTE STOCK':
    medicaments_alerte.append(m2_nom)
if m3_statut == 'ALERTE STOCK':
    medicaments_alerte.append(m3_nom)
if m4_statut == 'ALERTE STOCK':
    medicaments_alerte.append(m4_nom)
if m5_statut == 'ALERTE STOCK':
    medicaments_alerte.append(m5_nom)

# --- AFFICHAGE RAPPORT ---
# S2 (reutilise) : f-strings structurees
# S3 (nouveau) : statuts et couleurs determines par les conditions

print('\n' + '=' * 65)
print('  RAPPORT DE STOCK — PHARMACIE NATIONALE D\'APPROVISIONNEMENT')
print('  Date : 15 janvier 2026')
print('=' * 65)

print(f'\n  {m1_couleur} {m1_nom}')
print(f'      Stock : {m1_stock} unites  |  Seuil rupture : {m1_seuil_rupture}')
print(f'      Statut : {m1_statut}')
print(f'      Action : {m1_action}')
print('-' * 65)

print(f'\n  {m2_couleur} {m2_nom}')
print(f'      Stock : {m2_stock} unites  |  Seuil rupture : {m2_seuil_rupture}')
print(f'      Statut : {m2_statut}')
print(f'      Action : {m2_action}')
print('-' * 65)

print(f'\n  {m3_couleur} {m3_nom}')
print(f'      Stock : {m3_stock} unites  |  Seuil rupture : {m3_seuil_rupture}')
print(f'      Statut : {m3_statut}')
print(f'      Action : {m3_action}')
print('-' * 65)

print(f'\n  {m4_couleur} {m4_nom}')
print(f'      Stock : {m4_stock} unites  |  Seuil rupture : {m4_seuil_rupture}')
print(f'      Statut : {m4_statut}')
print(f'      Action : {m4_action}')
print('-' * 65)

print(f'\n  {m5_couleur} {m5_nom}')
print(f'      Stock : {m5_stock} unites  |  Seuil rupture : {m5_seuil_rupture}')
print(f'      Statut : {m5_statut}')
print(f'      Action : {m5_action}')
print('-' * 65)

# --- BILAN FINAL ---
print('\n' + '=' * 65)
print('  BILAN STOCK — PNA CONGO')
print('=' * 65)
print(f'  Ruptures critiques : {nb_ruptures_critiques}  ({", ".join(medicaments_rupture) if medicaments_rupture else "Aucune"})')
print(f'  Alertes stock      : {nb_alertes_stock}  ({", ".join(medicaments_alerte) if medicaments_alerte else "Aucune"})')
print(f'  Stocks normaux     : {nb_stocks_normaux}  ({m3_nom})')
print('=' * 65)

# --- ALERTE PRIORITAIRE ---
if nb_ruptures_critiques > 0:
    print('\n  !! ALERTE PRIORITAIRE : {} medicaments en RUPTURE CRITIQUE !!'.format(nb_ruptures_critiques))
    print(f'  Medicaments concernes : {", ".join(medicaments_rupture)}')
    print('  Transmettre immediatement au Dr. MOUKALA (PNA)')
    print('=' * 65)
else:
    print('\n  ✓ Aucune rupture critique detectee')
    print('=' * 65)

# ============================================================
# BONUS AVANCE : Classification avec operateur ternaire
# ============================================================

print('\n' + '=' * 65)
print('  BONUS : CLASSIFICATION AVEC OPERATEUR TERNAIRE')
print('=' * 65)

# Fonction de classification avec operateur ternaire imbrique
def classer_medicament(nom, stock, seuil):
    """
    Classifie un medicament en utilisant l'operateur ternaire imbrique.
    """
    statut, couleur, action = (
        ('RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h')
        if stock <= seuil else
        ('ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h')
        if stock <= seuil * 1.5 else
        ('STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee — planifier commande')
        if stock <= seuil * 2.0 else
        ('STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard')
    )
    return statut, couleur, action

# Tester la fonction avec les 5 medicaments
print("\n--- Test avec operateur ternaire ---")
for i, (nom, stock, seuil) in enumerate([
    (m1_nom, m1_stock, m1_seuil_rupture),
    (m2_nom, m2_stock, m2_seuil_rupture),
    (m3_nom, m3_stock, m3_seuil_rupture),
    (m4_nom, m4_stock, m4_seuil_rupture),
    (m5_nom, m5_stock, m5_seuil_rupture)
], 1):
    statut, couleur, action = classer_medicament(nom, stock, seuil)
    print(f"  {i}. {couleur} {nom}")
    print(f"     Stock: {stock} | Seuil: {seuil} | Statut: {statut}")

# ============================================================
# BONUS AVANCE : Saisie dynamique avec input()
# ============================================================

print('\n' + '=' * 65)
print('  BONUS : SAISIE DYNAMIQUE D\'UN MEDICAMENT')
print('=' * 65)

def saisir_medicament():
    """
    Permet a l'utilisateur de saisir un nouveau medicament et affiche son statut.
    Gere les erreurs de saisie.
    """
    print("\n--- Saisie d'un nouveau medicament ---")
    
    try:
        nom = input("Nom du medicament : ")
        stock = int(input("Stock disponible (unites) : "))
        seuil = int(input("Seuil de rupture (unites) : "))
        
        # Vérification des valeurs
        if stock < 0 or seuil < 0:
            print("Erreur : Les valeurs doivent etre positives")
            return
        
        # Classification
        statut, couleur, action = classer_medicament(nom, stock, seuil)
        
        # Affichage du resultat
        print("\n" + "-" * 40)
        print(f"  {couleur} {nom}")
        print(f"      Stock : {stock} unites | Seuil : {seuil}")
        print(f"      Statut : {statut}")
        print(f"      Action : {action}")
        print("-" * 40)
        
        # Alerte si rupture critique
        if statut == 'RUPTURE CRITIQUE':
            print("  !! ALERTE : Rupture critique immediate !!")
        
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides")

# Demander a l'utilisateur s'il veut tester le bonus
try:
    test_bonus = input("\nVoulez-vous tester la saisie dynamique ? (o/n) : ").lower()
    if test_bonus in ['o', 'oui', 'y', 'yes']:
        saisir_medicament()
except:
    print("\nTest du bonus ignore")

# ============================================================
# TESTS DES CAS LIMITES (EDGE CASES)
# ============================================================

print('\n' + '=' * 65)
print('  TESTS DES CAS LIMITES')
print('=' * 65)

# Test 1 : Stock exactement egal au seuil de rupture
print("\n1. Test : Stock == Seuil de rupture")
nom_test = "Test Exact Seuil"
stock_test = 2000
seuil_test = 2000
statut, couleur, action = classer_medicament(nom_test, stock_test, seuil_test)
print(f"   {couleur} {nom_test}")
print(f"   Stock: {stock_test} | Seuil: {seuil_test}")
print(f"   Statut: {statut}")
print(f"   Verdict: {'OK (<= declenche la rupture)' if statut == 'RUPTURE CRITIQUE' else 'ERREUR'}")

# Test 2 : Stock exactement egal a seuil * 1.5
print("\n2. Test : Stock == Seuil * 1.5")
nom_test = "Test Exact Alerte"
stock_test = 3000
seuil_test = 2000
statut, couleur, action = classer_medicament(nom_test, stock_test, seuil_test)
print(f"   {couleur} {nom_test}")
print(f"   Stock: {stock_test} | Seuil: {seuil_test}")
print(f"   Statut: {statut}")
print(f"   Verdict: {'OK (<= 1.5*seuil declenche alerte)' if statut == 'ALERTE STOCK' else 'ERREUR'}")

# Test 3 : Stock exactement egal a seuil * 2.0
print("\n3. Test : Stock == Seuil * 2.0")
nom_test = "Test Exact Limite"
stock_test = 4000
seuil_test = 2000
statut, couleur, action = classer_medicament(nom_test, stock_test, seuil_test)
print(f"   {couleur} {nom_test}")
print(f"   Stock: {stock_test} | Seuil: {seuil_test}")
print(f"   Statut: {statut}")
print(f"   Verdict: {'OK (<= 2.0*seuil declenche stock limite)' if statut == 'STOCK LIMITE' else 'ERREUR'}")

# Test 4 : Stock juste au-dessus de seuil * 2.0
print("\n4. Test : Stock > Seuil * 2.0")
nom_test = "Test Normal"
stock_test = 4001
seuil_test = 2000
statut, couleur, action = classer_medicament(nom_test, stock_test, seuil_test)
print(f"   {couleur} {nom_test}")
print(f"   Stock: {stock_test} | Seuil: {seuil_test}")
print(f"   Statut: {statut}")
print(f"   Verdict: {'OK (> 2.0*seuil donne stock normal)' if statut == 'STOCK NORMAL' else 'ERREUR'}")

print('\n' + '=' * 65)
print('  FIN DU RAPPORT')
print('=' * 65)