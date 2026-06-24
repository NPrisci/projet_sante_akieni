# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Challenge : Rapport d'Etat Sanitaire Departemental
# Notions S2 : variables, types, operateurs, f-strings
# Notions S3 : if/elif/else, conditions composees (and/or)
# ============================================================

# --- CONSTANTES ---
SEUIL_OCCUPATION_OPTIMAL_MIN = 70.0    # % minimum optimal
SEUIL_OCCUPATION_OPTIMAL_MAX = 85.0    # % maximum optimal
SEUIL_OCCUPATION_ALERTE = 85.0         # % alerte occupation
SEUIL_OCCUPATION_CRITIQUE = 95.0       # % critique occupation
COUT_COMMANDE_EXPRESS = 450_000.0      # FCFA

# --- DONNEES DES 5 HOPITAUX ---

# Hopital 1 - CHU Brazzaville
h1_nom = 'CHU Brazzaville'
h1_lits_total = 320
h1_lits_occupes = 298
h1_nb_medecins = 47
h1_meds_rupture = 2      # SRO, Vaccin
h1_meds_alerte = 2       # Artemether, Amoxi

# Hopital 2 - Hopital General Pointe-Noire
h2_nom = 'Hopital Pointe-Noire'
h2_lits_total = 180
h2_lits_occupes = 143
h2_nb_medecins = 22
h2_meds_rupture = 0
h2_meds_alerte = 1       # Amoxicilline

# Hopital 3 - Hopital de Dolisie
h3_nom = 'Hopital Dolisie'
h3_lits_total = 95
h3_lits_occupes = 91
h3_nb_medecins = 8
h3_meds_rupture = 1      # SRO
h3_meds_alerte = 2       # Artemether, Vaccin

# Hopital 4 - Hopital de district Owando
h4_nom = 'Hopital Owando'
h4_lits_total = 45
h4_lits_occupes = 32
h4_nb_medecins = 3
h4_meds_rupture = 3      # SRO, Vaccin, Artemether
h4_meds_alerte = 0

# Hopital 5 - CMS Impfondo
h5_nom = 'CMS Impfondo'
h5_lits_total = 20
h5_lits_occupes = 19
h5_nb_medecins = 1
h5_meds_rupture = 2      # SRO, Amoxi
h5_meds_alerte = 1       # Vaccin

# --- FONCTION DE CALCUL DU TAUX D'OCCUPATION ---

def calculer_taux_occupation(lits_occupes: int, lits_total: int) -> float:
    """
    Calcule le taux d'occupation des lits
    
    Args:
        lits_occupes: Nombre de lits occupes
        lits_total: Nombre total de lits
    
    Returns:
        float: Taux d'occupation en pourcentage
    """
    if lits_total == 0:
        return 0.0
    return (lits_occupes / lits_total) * 100

# --- FONCTION DE DETERMINATION DU NIVEAU D'OCCUPATION ---

def determiner_niveau_occupation(taux_occupation: float) -> dict:
    """
    Determine le niveau d'occupation selon les seuils definis
    
    Args:
        taux_occupation: Taux d'occupation en pourcentage
    
    Returns:
        dict: Contenant le niveau, la couleur et l'interpretation
    """
    if taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
        return {
            'niveau': 'CRITIQUE',
            'couleur': '[ROUGE]',
            'code': 'CRI',
            'interpretation': 'Surcharge critique des lits'
        }
    elif taux_occupation > SEUIL_OCCUPATION_ALERTE:
        return {
            'niveau': 'ALERTE',
            'couleur': '[ORANGE]',
            'code': 'ALT',
            'interpretation': 'Surcharge des lits'
        }
    elif SEUIL_OCCUPATION_OPTIMAL_MIN <= taux_occupation <= SEUIL_OCCUPATION_OPTIMAL_MAX:
        return {
            'niveau': 'OPTIMAL',
            'couleur': '[VERT]',
            'code': 'OK',
            'interpretation': 'Taux d\'occupation optimal'
        }
    else:
        return {
            'niveau': 'SOUS-UTILISE',
            'couleur': '[JAUNE]',
            'code': 'SOUS',
            'interpretation': 'Sous-utilisation des lits'
        }

# --- FONCTION DE DETERMINATION DU NIVEAU GLOBAL ---

def determiner_niveau_global(nb_ruptures: int, nb_alertes: int, 
                            taux_occupation: float, nb_medecins: int) -> dict:
    """
    Determine le niveau d'alerte global selon les regles definies
    
    Args:
        nb_ruptures: Nombre de medicaments en rupture
        nb_alertes: Nombre de medicaments en alerte
        taux_occupation: Taux d'occupation en pourcentage
        nb_medecins: Nombre de medecins
    
    Returns:
        dict: Contenant le niveau et la recommandation
    """
    # Niveau CRITIQUE
    if nb_ruptures >= 2 or taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
        return {
            'niveau': 'CRITIQUE',
            'couleur': '[ROUGE]',
            'recommandation': 'Mobiliser la reserve nationale PNA'
        }
    
    # Niveau PREOCCUPANT
    elif (nb_ruptures >= 1 or 
          taux_occupation > SEUIL_OCCUPATION_ALERTE or 
          (nb_alertes >= 2 and nb_medecins < 5)):
        return {
            'niveau': 'PREOCCUPANT',
            'couleur': '[ORANGE]',
            'recommandation': 'Renforcer la surveillance et planifier des actions'
        }
    
    # Niveau SATISFAISANT
    else:
        return {
            'niveau': 'SATISFAISANT',
            'couleur': '[VERT]',
            'recommandation': 'Maintenir le suivi standard'
        }

# --- CALCUL POUR CHAQUE HOPITAL ---

# Hopital 1
taux_occ_h1 = calculer_taux_occupation(h1_lits_occupes, h1_lits_total)
niveau_occ_h1 = determiner_niveau_occupation(taux_occ_h1)
niveau_global_h1 = determiner_niveau_global(h1_meds_rupture, h1_meds_alerte, 
                                            taux_occ_h1, h1_nb_medecins)

# Hopital 2
taux_occ_h2 = calculer_taux_occupation(h2_lits_occupes, h2_lits_total)
niveau_occ_h2 = determiner_niveau_occupation(taux_occ_h2)
niveau_global_h2 = determiner_niveau_global(h2_meds_rupture, h2_meds_alerte, 
                                            taux_occ_h2, h2_nb_medecins)

# Hopital 3
taux_occ_h3 = calculer_taux_occupation(h3_lits_occupes, h3_lits_total)
niveau_occ_h3 = determiner_niveau_occupation(taux_occ_h3)
niveau_global_h3 = determiner_niveau_global(h3_meds_rupture, h3_meds_alerte, 
                                            taux_occ_h3, h3_nb_medecins)

# Hopital 4
taux_occ_h4 = calculer_taux_occupation(h4_lits_occupes, h4_lits_total)
niveau_occ_h4 = determiner_niveau_occupation(taux_occ_h4)
niveau_global_h4 = determiner_niveau_global(h4_meds_rupture, h4_meds_alerte, 
                                            taux_occ_h4, h4_nb_medecins)

# Hopital 5
taux_occ_h5 = calculer_taux_occupation(h5_lits_occupes, h5_lits_total)
niveau_occ_h5 = determiner_niveau_occupation(taux_occ_h5)
niveau_global_h5 = determiner_niveau_global(h5_meds_rupture, h5_meds_alerte, 
                                            taux_occ_h5, h5_nb_medecins)

# --- BILAN NATIONAL ---

# Compter les hopitaux par niveau
hopitaux_critiques = 0
hopitaux_preoccupants = 0
hopitaux_satisfaisants = 0

if niveau_global_h1['niveau'] == 'CRITIQUE':
    hopitaux_critiques += 1
elif niveau_global_h1['niveau'] == 'PREOCCUPANT':
    hopitaux_preoccupants += 1
else:
    hopitaux_satisfaisants += 1

if niveau_global_h2['niveau'] == 'CRITIQUE':
    hopitaux_critiques += 1
elif niveau_global_h2['niveau'] == 'PREOCCUPANT':
    hopitaux_preoccupants += 1
else:
    hopitaux_satisfaisants += 1

if niveau_global_h3['niveau'] == 'CRITIQUE':
    hopitaux_critiques += 1
elif niveau_global_h3['niveau'] == 'PREOCCUPANT':
    hopitaux_preoccupants += 1
else:
    hopitaux_satisfaisants += 1

if niveau_global_h4['niveau'] == 'CRITIQUE':
    hopitaux_critiques += 1
elif niveau_global_h4['niveau'] == 'PREOCCUPANT':
    hopitaux_preoccupants += 1
else:
    hopitaux_satisfaisants += 1

if niveau_global_h5['niveau'] == 'CRITIQUE':
    hopitaux_critiques += 1
elif niveau_global_h5['niveau'] == 'PREOCCUPANT':
    hopitaux_preoccupants += 1
else:
    hopitaux_satisfaisants += 1

# Total des ruptures et alertes nationales
total_ruptures_national = (h1_meds_rupture + h2_meds_rupture + 
                          h3_meds_rupture + h4_meds_rupture + h5_meds_rupture)
total_alertes_national = (h1_meds_alerte + h2_meds_alerte + 
                         h3_meds_alerte + h4_meds_alerte + h5_meds_alerte)

# Cout des commandes urgentes (BONUS)
cout_commandes_express = total_ruptures_national * COUT_COMMANDE_EXPRESS

# --- AFFICHAGE DU RAPPORT ---

print('=' * 85)
print('  TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE')
print('  Date : 16 janvier 2026 | Pour le Conseil des Ministres')
print('=' * 85)
print()

# En-tete du tableau
print(f"{'HOPITAL':<25} {'OCCUPATION':>12} {'ALERTES':>12} {'MEDECINS':>10} {'NIVEAU GLOBAL':>15}")
print(f"{'':25} {'':12} {'R/A':>12} {'':10} {'':15}")
print('-' * 85)

# Lignes du tableau
hopitaux_data = [
    (h1_nom, taux_occ_h1, niveau_occ_h1, h1_meds_rupture, h1_meds_alerte, 
     h1_nb_medecins, niveau_global_h1),
    (h2_nom, taux_occ_h2, niveau_occ_h2, h2_meds_rupture, h2_meds_alerte, 
     h2_nb_medecins, niveau_global_h2),
    (h3_nom, taux_occ_h3, niveau_occ_h3, h3_meds_rupture, h3_meds_alerte, 
     h3_nb_medecins, niveau_global_h3),
    (h4_nom, taux_occ_h4, niveau_occ_h4, h4_meds_rupture, h4_meds_alerte, 
     h4_nb_medecins, niveau_global_h4),
    (h5_nom, taux_occ_h5, niveau_occ_h5, h5_meds_rupture, h5_meds_alerte, 
     h5_nb_medecins, niveau_global_h5),
]

for nom, taux_occ, niveau_occ, ruptures, alertes, medecins, niveau_global in hopitaux_data:
    # Formatage du taux d'occupation avec niveau
    occ_str = f"{taux_occ:.1f}% [{niveau_occ['code']}]"
    
    # Formatage des alertes
    alertes_str = f"{ruptures}R + {alertes}A"
    
    # Formatage du niveau global
    niveau_str = f"{niveau_global['couleur']} {niveau_global['niveau']}"
    
    print(f"{nom:<25} {occ_str:>12} {alertes_str:>12} {medecins:>10} {niveau_str:>15}")

print('-' * 85)
print()

# --- ANALYSE ET RECOMMANDATIONS ---

print('ANALYSE SECTORIELLE')
print('-' * 85)

# Nombre d'hopitaux en situation critique
print(f"  {hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
print(f"  {hopitaux_preoccupants} hopitaux en situation PREOCCUPANTE")
print(f"  {hopitaux_satisfaisants} hopitaux en situation SATISFAISANTE")
print()

# Total des ruptures
print(f"  {total_ruptures_national} ruptures de stock identifiees a l'echelle nationale")
print(f"  {total_alertes_national} alertes de stock recensees")
print()

# BONUS : Cout des commandes urgentes
print('ANALYSE BUDGETAIRE — COMMANDES URGENTES')
print('-' * 85)
print(f"  Cout moyen d'une commande express : {COUT_COMMANDE_EXPRESS:,.0f} FCFA".replace(',', ' '))
print(f"  Nombre de commandes express necessaires : {total_ruptures_national}")
print(f"  Cout total estime : {cout_commandes_express:,.0f} FCFA".replace(',', ' '))
print(f"  Soit : {cout_commandes_express / 655.957:,.2f} EUR".replace(',', ' '))
print(f"  Soit : {cout_commandes_express / 600.0:,.2f} USD".replace(',', ' '))
print()

# --- RECOMMANDATION PRIORITAIRE ---

print('RECOMMANDATION PRIORITAIRE')
print('-' * 85)

# Identifier la recommendation la plus critique
recommendations = []
for nom, niveau_global in [
    (h1_nom, niveau_global_h1),
    (h2_nom, niveau_global_h2),
    (h3_nom, niveau_global_h3),
    (h4_nom, niveau_global_h4),
    (h5_nom, niveau_global_h5),
]:
    if niveau_global['niveau'] == 'CRITIQUE':
        recommendations.append(f"{nom} : {niveau_global['recommandation']}")

if recommendations:
    print("  ACTIONS URGENTES :")
    for rec in recommendations:
        print(f"    • {rec}")
else:
    print("  ✓ Aucune action urgente requise")

print()

# Recommendation globale
if hopitaux_critiques >= 3:
    print("  🚨 RECOMMANDATION GLOBALE : Mobiliser la reserve nationale PNA")
    print("  → Activer le plan d'urgence national")
    print("  → Deployment d'equipes mobiles dans les hopitaux critiques")
elif hopitaux_critiques >= 1:
    print("  ⚠️ RECOMMANDATION GLOBALE : Renforcer les hopitaux critiques")
    print("  → Prioriser les hopitaux avec multiples ruptures")
    print("  → Augmenter les quotas de medicaments")
else:
    print("  ✓ RECOMMANDATION GLOBALE : Maintenir le suivi standard")
    print("  → Surveillance continue des indicateurs")
    print("  → Planification proactive des approvisionnements")

print('=' * 85)
print('  FIN DU RAPPORT — A TRANSMETTRE AU CONSEIL DES MINISTRES')
print('=' * 85)

# ============================================================
# BONUS : DETAIL PAR HOPITAL
# ============================================================

print('\n' + '=' * 85)
print('  DETAIL PAR HOPITAL — NIVEAUX D\'OCCUPATION ET ALERTES')
print('=' * 85)
print()

# Fonction pour afficher le detail d'un hopital
def afficher_detail_hopital(nom, taux_occ, niveau_occ, ruptures, alertes, 
                           medecins, niveau_global):
    """Affiche le detail d'un hopital"""
    print(f"  {niveau_global['couleur']} {nom}")
    print(f"      Taux d'occupation : {taux_occ:.1f}% ({niveau_occ['niveau']})")
    print(f"      Lits : {lits_occupes}/{lits_total} occupes")
    print(f"      Medicaments : {ruptures} rupture(s), {alertes} alerte(s)")
    print(f"      Medecins : {medecins}")
    print(f"      Niveau global : {niveau_global['niveau']}")
    print(f"      Action : {niveau_global['recommandation']}")
    print()

# Affichage du detail pour chaque hopital
for nom, lits_occupes, lits_total, taux_occ, niveau_occ, ruptures, alertes, medecins, niveau_global in [
    (h1_nom, h1_lits_occupes, h1_lits_total, taux_occ_h1, niveau_occ_h1, 
     h1_meds_rupture, h1_meds_alerte, h1_nb_medecins, niveau_global_h1),
    (h2_nom, h2_lits_occupes, h2_lits_total, taux_occ_h2, niveau_occ_h2, 
     h2_meds_rupture, h2_meds_alerte, h2_nb_medecins, niveau_global_h2),
    (h3_nom, h3_lits_occupes, h3_lits_total, taux_occ_h3, niveau_occ_h3, 
     h3_meds_rupture, h3_meds_alerte, h3_nb_medecins, niveau_global_h3),
    (h4_nom, h4_lits_occupes, h4_lits_total, taux_occ_h4, niveau_occ_h4, 
     h4_meds_rupture, h4_meds_alerte, h4_nb_medecins, niveau_global_h4),
    (h5_nom, h5_lits_occupes, h5_lits_total, taux_occ_h5, niveau_occ_h5, 
     h5_meds_rupture, h5_meds_alerte, h5_nb_medecins, niveau_global_h5),
]:
    afficher_detail_hopital(nom, taux_occ, niveau_occ, ruptures, alertes, 
                           medecins, niveau_global)

print('=' * 85)
print('  FIN DU RAPPORT DETAILLE')
print('=' * 85)