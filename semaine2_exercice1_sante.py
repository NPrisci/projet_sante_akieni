# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville 
# Votre nom : NOUDOFININ Priscillia 
# Date      : 23/06/2026
# ============================================================ 

# ============================================================
# CONSEIL 1 : Commencez par écrire toutes les variables avant 
# d'écrire la moindre ligne de calcul
# ============================================================

# --- SECTION 1 : VARIABLES PATIENT --- 
nom_patient = 'MAVOUNGOU Celestine'     # str - Nom complet en majuscules
age_patient = 42                         # int - Age en annees entieres
sexe_patient = 'F'                       # str - F pour Femme, M pour Homme
departement_patient = 'Brazzaville'      # str - Departement de residence
couverture_sociale = 'CNSS'              # str - Type de couverture sociale

# --- SECTION 2 : VARIABLES CONSULTATION --- 
type_consultation = 'Urgences'           # str - Type de consultation
cout_consultation_fcfa = 15000.0         # float - Cout unitaire en FCFA
nb_consultations = 1                     # int - Nombre de consultations
remise_cnss_pct = 30.0                   # float - Pourcentage de remise CNSS
diagnostic_principal = 'Paludisme grave' # str - Diagnostic CIM-10

# --- SECTION 3 : VARIABLES HOPITAL --- 
nom_hopital = 'CHU de Brazzaville'       # str - Nom officiel de l'hopital
ville_hopital = 'Brazzaville'            # str - Ville d'implantation
nb_lits_total = 320                      # int - Capacite totale en lits
nb_lits_occupes = 284                    # int - Lits actuellement occupes
nb_medecins_actifs = 47                  # int - Medecins presents ce jour

# ============================================================
# CONSEIL 2 : Après chaque variable, ajoutez type() pour 
# vérifier le type
# ============================================================

print("=== VERIFICATION DES TYPES (CONSEIL 2) ===")
print(f"nom_patient: {type(nom_patient)} → {nom_patient}")
print(f"age_patient: {type(age_patient)} → {age_patient}")
print(f"sexe_patient: {type(sexe_patient)} → {sexe_patient}")
print(f"departement_patient: {type(departement_patient)} → {departement_patient}")
print(f"couverture_sociale: {type(couverture_sociale)} → {couverture_sociale}")
print(f"type_consultation: {type(type_consultation)} → {type_consultation}")
print(f"cout_consultation_fcfa: {type(cout_consultation_fcfa)} → {cout_consultation_fcfa}")
print(f"nb_consultations: {type(nb_consultations)} → {nb_consultations}")
print(f"remise_cnss_pct: {type(remise_cnss_pct)} → {remise_cnss_pct}")
print(f"diagnostic_principal: {type(diagnostic_principal)} → {diagnostic_principal}")
print(f"nom_hopital: {type(nom_hopital)} → {nom_hopital}")
print(f"ville_hopital: {type(ville_hopital)} → {ville_hopital}")
print(f"nb_lits_total: {type(nb_lits_total)} → {nb_lits_total}")
print(f"nb_lits_occupes: {type(nb_lits_occupes)} → {nb_lits_occupes}")
print(f"nb_medecins_actifs: {type(nb_medecins_actifs)} → {nb_medecins_actifs}")
print("\n" + "="*60 + "\n")

# ============================================================
# CONSEIL 3 : Testez chaque calcul isolé avant de l'intégrer 
# dans l'affichage
# ============================================================

# --- SECTION 4 : CALCULS --- 

# CALCUL 1 : Cout total après remise CNSS
# Test isolé du calcul 1
print("=== TEST CALCUL 1 : Cout total ===")
print(f"cout_consultation_fcfa = {cout_consultation_fcfa}")
print(f"nb_consultations = {nb_consultations}")
print(f"remise_cnss_pct = {remise_cnss_pct}%")
print(f"remise en decimal = {remise_cnss_pct / 100}")
print(f"taux a payer = {1 - remise_cnss_pct / 100}")
cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)
print(f"cout_total_fcfa = {cout_total_fcfa}")
print(f"Vérification : 15000 * 1 * 0.70 = {15000 * 1 * 0.70}")
print("\n" + "="*60 + "\n")

# CALCUL 2 : Taux d'occupation
# Test isolé du calcul 2
print("=== TEST CALCUL 2 : Taux d'occupation ===")
print(f"nb_lits_occupes = {nb_lits_occupes}")
print(f"nb_lits_total = {nb_lits_total}")
print(f"ratio = {nb_lits_occupes / nb_lits_total}")
print(f"en pourcentage = {(nb_lits_occupes / nb_lits_total) * 100}")
taux_occupation_pct = round((nb_lits_occupes / nb_lits_total) * 100, 1)
print(f"taux_occupation_pct (arrondi) = {taux_occupation_pct}")
print(f"Vérification : (284/320)*100 = 88.75 → arrondi à {round(88.75, 1)}")
print("\n" + "="*60 + "\n")

# CALCUL 3 : Ratio consultations par médecin
# Test isolé du calcul 3
print("=== TEST CALCUL 3 : Ratio consultations/médecin ===")
nb_consultations_hopital = 120  # Hypothèse : 120 consultations ce matin
print(f"nb_consultations_hopital = {nb_consultations_hopital}")
print(f"nb_medecins_actifs = {nb_medecins_actifs}")
print(f"ratio = {nb_consultations_hopital / nb_medecins_actifs}")
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)
print(f"ratio_consultations_medecin (arrondi) = {ratio_consultations_medecin}")
print(f"Vérification : 120/47 = 2.553... → arrondi à {round(2.553, 1)}")
print("\n" + "="*60 + "\n")

# ============================================================
# CONSEIL 4 : Pour les f-strings longues, utilisez des 
# variables intermédiaires pour plus de lisibilité
# ============================================================

# --- SECTION 5 : AFFICHAGE AVEC VARIABLES INTERMEDIAIRES --- 

# Construction des variables intermédiaires pour l'affichage
titre_fiche = f"FICHE PATIENT — {nom_patient}"
ligne_separateur = "=" * 60

# Informations patient formatées
info_patient = f"""Age : {age_patient} ans
Sexe : {sexe_patient}
Departement : {departement_patient}
Couverture : {couverture_sociale}"""

# Informations consultation formatées
# Utilisation de replace pour remplacer les virgules par des espaces
cout_unitaire_formate = f"{cout_consultation_fcfa:,.0f} FCFA".replace(',', ' ')
cout_total_formate = f"{cout_total_fcfa:,.1f} FCFA".replace(',', ' ')

info_consultation = f"""Type : {type_consultation}
Diagnostic : {diagnostic_principal}
Cout unitaire : {cout_unitaire_formate}
Remise CNSS : {remise_cnss_pct}%
COUT TOTAL : {cout_total_formate}"""

# Informations hôpital formatées
info_hopital = f"""HOPITAL : {nom_hopital}
Ville : {ville_hopital}
Lits occupes : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)
Medecins actifs : {nb_medecins_actifs}
Ratio consult. : {ratio_consultations_medecin} consultations / medecin ce matin"""

# ============================================================
# AFFICHAGE FINAL AVEC LES VARIABLES INTERMEDIAIRES
# ============================================================

print(ligne_separateur)
print(f"  {titre_fiche}")
print(ligne_separateur)
print(info_patient)
print()
print("CONSULTATION")
print(info_consultation)
print()
print(info_hopital)
print()
print("STATUT : Prise en charge validée")
print(ligne_separateur)

# ============================================================
# BONUS AVANCÉ — Saisie utilisateur avec gestion d'erreurs
# ============================================================

print("\n" + "="*60)
print("=== BONUS AVANCÉ : SAISIE UTILISATEUR ===")
print("="*60 + "\n")

def saisir_entier(message, min_val=None, max_val=None):
    """
    Saisie sécurisée d'un entier avec gestion d'erreurs
    
    Args:
        message (str): Message à afficher à l'utilisateur
        min_val (int, optional): Valeur minimale acceptée
        max_val (int, optional): Valeur maximale acceptée
    
    Returns:
        int: La valeur saisie et validée
    """
    while True:
        try:
            valeur = input(message)
            valeur = int(valeur)
            
            if min_val is not None and valeur < min_val:
                print(f"Erreur : La valeur doit être supérieure ou égale à {min_val}")
                continue
            if max_val is not None and valeur > max_val:
                print(f"Erreur : La valeur doit être inférieure ou égale à {max_val}")
                continue
                
            return valeur
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide (ex: 42)")

def saisir_float(message, min_val=None, max_val=None):
    """
    Saisie sécurisée d'un nombre décimal avec gestion d'erreurs
    
    Args:
        message (str): Message à afficher à l'utilisateur
        min_val (float, optional): Valeur minimale acceptée
        max_val (float, optional): Valeur maximale acceptée
    
    Returns:
        float: La valeur saisie et validée
    """
    while True:
        try:
            valeur = input(message)
            valeur = float(valeur)
            
            if min_val is not None and valeur < min_val:
                print(f"Erreur : La valeur doit être supérieure ou égale à {min_val}")
                continue
            if max_val is not None and valeur > max_val:
                print(f"Erreur : La valeur doit être inférieure ou égale à {max_val}")
                continue
                
            return valeur
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide (ex: 42.5)")

def saisir_oui_non(message):
    """
    Saisie sécurisée d'une réponse oui/non
    
    Args:
        message (str): Message à afficher à l'utilisateur
    
    Returns:
        bool: True si oui, False si non
    """
    while True:
        reponse = input(message + " (o/n) : ").lower()
        if reponse in ['o', 'oui', 'y', 'yes']:
            return True
        elif reponse in ['n', 'non', 'n', 'no']:
            return False
        else:
            print("Erreur : Veuillez répondre par 'o' (oui) ou 'n' (non)")

# --- TEST DU BONUS ---
print("=== TEST DU BONUS AVANCÉ ===\n")
print("Test 1 : Saisie de l'âge (avec validation)")
age_saisi = saisir_entier("Entrez l'âge du patient : ", min_val=0, max_val=150)
print(f"Âge saisi : {age_saisi} ans\n")

print("Test 2 : Saisie du coût (avec validation)")
cout_saisi = saisir_float("Entrez le coût de la consultation (FCFA) : ", min_val=0)
print(f"Coût saisi : {cout_saisi} FCFA\n")

print("Test 3 : Saisie d'une réponse oui/non")
confirmation = saisir_oui_non("Confirmez-vous ces informations ?")
print(f"Confirmation : {'Oui' if confirmation else 'Non'}\n")

print("Test 4 : Test avec entrée non numérique")
print("Essayez d'entrer 'quarante-deux' quand on vous demande un nombre...")
print("Le programme devrait gérer l'erreur sans planter")
age_test = saisir_entier("Entrez un nombre (test) : ")
print(f"Résultat : {age_test}")

# ============================================================
# BONUS 2 : Simulation d'une base de patients
# ============================================================

print("\n" + "="*60)
print("=== BONUS 2 : SIMULATION BASE DE PATIENTS ===")
print("="*60 + "\n")

def creer_fiche_patient(nom, age, sexe, departement, couverture, 
                       type_consult, cout, nb_consult, remise, diagnostic,
                       hopital, ville, lits_total, lits_occupes, medecins):
    """
    Fonction qui crée une fiche patient à partir des données fournies
    """
    # Calculs
    cout_total = cout * nb_consult * (1 - remise / 100)
    taux_occup = round((lits_occupes / lits_total) * 100, 1)
    
    # Affichage
    print("="*60)
    print(f"  FICHE PATIENT — {nom}")
    print("="*60)
    print(f"Age : {age} ans")
    print(f"Sexe : {sexe}")
    print(f"Departement : {departement}")
    print(f"Couverture : {couverture}")
    print()
    print("CONSULTATION")
    print(f"Type : {type_consult}")
    print(f"Diagnostic : {diagnostic}")
    print(f"Cout unitaire : {cout:,.0f} FCFA".replace(',', ' '))
    print(f"Remise : {remise}%")
    print(f"COUT TOTAL : {cout_total:,.1f} FCFA".replace(',', ' '))
    print()
    print(f"HOPITAL : {hopital}")
    print(f"Ville : {ville}")
    print(f"Lits occupes : {lits_occupes} / {lits_total} ({taux_occup}%)")
    print(f"Medecins actifs : {medecins}")
    print()
    print("STATUT : Prise en charge validée")
    print("="*60)
    print()

# Test avec plusieurs patients
patients = [
    {
        'nom': 'MAVOUNGOU Celestine',
        'age': 42,
        'sexe': 'F',
        'departement': 'Brazzaville',
        'couverture': 'CNSS',
        'type_consult': 'Urgences',
        'cout': 15000.0,
        'nb_consult': 1,
        'remise': 30.0,
        'diagnostic': 'Paludisme grave',
        'hopital': 'CHU de Brazzaville',
        'ville': 'Brazzaville',
        'lits_total': 320,
        'lits_occupes': 284,
        'medecins': 47
    },
    {
        'nom': 'NGOMA Jean-Pierre',
        'age': 65,
        'sexe': 'M',
        'departement': 'Pointe-Noire',
        'couverture': 'Mutuelle',
        'type_consult': 'Programme',
        'cout': 25000.0,
        'nb_consult': 2,
        'remise': 15.0,
        'diagnostic': 'Diabète type 2',
        'hopital': 'CHU de Pointe-Noire',
        'ville': 'Pointe-Noire',
        'lits_total': 250,
        'lits_occupes': 180,
        'medecins': 32
    }
]

print("=== SIMULATION DE PLUSIEURS PATIENTS ===\n")
for i, patient in enumerate(patients, 1):
    print(f"Patient {i} :")
    creer_fiche_patient(**patient)

# ============================================================
# CONSEIL 5 : Nettoyer et organiser son code (fait)
# ============================================================

print("="*60)
print("FIN DE L'EXERCICE 1 — FICHE PATIENT")
print("="*60)