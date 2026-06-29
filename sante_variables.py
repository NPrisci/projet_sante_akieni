# ============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# 
# VERSION : S3 — Ajout des classifications automatiques
# DATE    : 25 juin 2026
# ============================================================ 

# ============================================================
# SECTION A : CONSTANTES NATIONALES ET NORMES OMS (S2)
# ============================================================

# Taux de change
TAUX_EUR_FCFA = 655.957  # Taux fixe CFA
TAUX_USD_FCFA = 600.0    # Taux approximatif 2025

# Seuils OMS (en MAJUSCULES selon convention Python)
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_CRITIQUE_COUVERTURE = 50.0    # seuil zone critique
SEUIL_RISQUE_COUVERTURE = 80.0      # seuil zone a risque
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations
SEUIL_CRITIQUE_DENSITE = 0.05       # Densite critique pour alerte
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock

# Seuils d'occupation des lits
SEUIL_OCCUPATION_OPTIMAL_MIN = 70.0
SEUIL_OCCUPATION_OPTIMAL_MAX = 85.0
SEUIL_OCCUPATION_ALERTE = 85.0
SEUIL_OCCUPATION_CRITIQUE = 95.0

# 12 departements officiels du Congo
DEPARTEMENTS_CONGO = [
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# ============================================================
# SECTION B : VARIABLES DES 5 HOPITAUX (S2)
# ============================================================

# Hopital 1 — CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 298  # Modifié pour S3
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000
h1_budget_trimestriel = 45_000_000.0
h1_nb_consultations = 4_823
h1_nb_hospitalisations = 1_247
h1_nb_deces = 18
h1_taux_remise_cnss = 30.0

# Hopital 2 — Hopital General Pointe-Noire
h2_nom = 'Hopital General Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Kouilou'
h2_type = 'Hopital General'
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 128_000
h2_budget_trimestriel = 87_450_000.0
h2_nb_consultations = 4_823
h2_nb_hospitalisations = 1_247
h2_nb_deces = 18
h2_taux_remise_cnss = 30.0

# Hopital 3 — Hopital de Dolisie
h3_nom = 'Hopital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = 'Hopital Regional'
h3_nb_lits = 95
h3_nb_lits_occupes = 91  # Modifié pour S3
h3_nb_medecins = 8
h3_nb_infirmiers = 45
h3_population_zone = 95_000
h3_budget_trimestriel = 25_000_000.0
h3_nb_consultations = 2_156
h3_nb_hospitalisations = 587
h3_nb_deces = 9
h3_taux_remise_cnss = 25.0

# Hopital 4 — Hopital de district Owando
h4_nom = 'Hopital de district Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = 'Hopital de District'
h4_nb_lits = 45
h4_nb_lits_occupes = 32  # Modifié pour S3
h4_nb_medecins = 3
h4_nb_infirmiers = 32
h4_population_zone = 64_000
h4_budget_trimestriel = 14_500_000.0
h4_nb_consultations = 1_234
h4_nb_hospitalisations = 356
h4_nb_deces = 7
h4_taux_remise_cnss = 20.0

# Hopital 5 — Centre de sante de Impfondo
h5_nom = 'Centre de sante de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = 'Centre de Sante'
h5_nb_lits = 20
h5_nb_lits_occupes = 19  # Modifié pour S3
h5_nb_medecins = 1
h5_nb_infirmiers = 15
h5_population_zone = 35_000
h5_budget_trimestriel = 8_200_000.0
h5_nb_consultations = 678
h5_nb_hospitalisations = 189
h5_nb_deces = 5
h5_taux_remise_cnss = 15.0

# ============================================================
# SECTION C : VARIABLES DES 5 MEDICAMENTS (S2)
# ============================================================

# Medicament 1 — Antipaludique
m1_nom = 'Artemether-Lumefantrine'
m1_categorie = 'Antipaludique'
m1_quantite_disponible = 3200  # Modifié pour S3
m1_seuil_rupture = 2000
m1_cout_unitaire = 1500.0
m1_duree_stock_jours = 68

# Medicament 2 — Antibiotique
m2_nom = 'Amoxicilline 500mg'
m2_categorie = 'Antibiotique'
m2_quantite_disponible = 950  # Modifié pour S3
m2_seuil_rupture = 800
m2_cout_unitaire = 450.0
m2_duree_stock_jours = 45

# Medicament 3 — Antalgique
m3_nom = 'Paracetamol 500mg'
m3_categorie = 'Antalgique'
m3_quantite_disponible = 12400  # Modifié pour S3
m3_seuil_rupture = 3000
m3_cout_unitaire = 150.0
m3_duree_stock_jours = 30

# Medicament 4 — SRO (Soluté de Réhydratation Orale)
m4_nom = 'SRO (sachets)'
m4_categorie = 'Rehydratation'
m4_quantite_disponible = 4200  # Modifié pour S3
m4_seuil_rupture = 5000
m4_cout_unitaire = 200.0
m4_duree_stock_jours = 25

# Medicament 5 — Vaccin
m5_nom = 'Vaccin DTP-HepB-Hib'
m5_categorie = 'Vaccin'
m5_quantite_disponible = 820  # Modifié pour S3
m5_seuil_rupture = 1000
m5_cout_unitaire = 8500.0
m5_duree_stock_jours = 40

# ============================================================
# SECTION D : CALCULS D'INITIALISATION (S2)
# ============================================================

def calculer_kpis_hopital(nom, nb_lits, nb_lits_occupes, nb_medecins, 
                          population_zone, nb_hospitalisations, nb_deces, 
                          budget_trimestriel, nb_consultations):
    """
    Calcule les indicateurs clés pour un hopital
    
    Returns:
        dict: Dictionnaire contenant tous les KPIs
    """
    # Densité médicale (médecins pour 1000 habitants)
    if population_zone > 0:
        densite_medicale = (nb_medecins / population_zone) * 1000
    else:
        densite_medicale = 0.0
    
    # Taux d'occupation des lits (%)
    if nb_lits > 0:
        taux_occupation = (nb_lits_occupes / nb_lits) * 100
    else:
        taux_occupation = 0.0
    
    # Taux de mortalité hospitalière (%)
    if nb_hospitalisations > 0:
        taux_mortalite = (nb_deces / nb_hospitalisations) * 100
    else:
        taux_mortalite = 0.0
    
    # Coût moyen par patient (FCFA)
    if nb_consultations > 0:
        cout_moyen_patient = budget_trimestriel / nb_consultations
    else:
        cout_moyen_patient = 0.0
    
    # Status critique
    est_critique = (taux_mortalite > SEUIL_MORTALITE_ALERTE or 
                   densite_medicale < SEUIL_CRITIQUE_DENSITE)
    
    return {
        'nom': nom,
        'densite_medicale': round(densite_medicale, 2),
        'taux_occupation': round(taux_occupation, 1),
        'taux_mortalite': round(taux_mortalite, 1),
        'cout_moyen_patient': round(cout_moyen_patient, 0),
        'est_critique': est_critique,
        'nb_medecins': nb_medecins,
        'nb_lits': nb_lits,
        'nb_hospitalisations': nb_hospitalisations,
        'nb_deces': nb_deces
    }

# Regrouper tous les hopitaux dans une liste pour faciliter le traitement
hopitaux = [
    (h1_nom, h1_nb_lits, h1_nb_lits_occupes, h1_nb_medecins, 
     h1_population_zone, h1_nb_hospitalisations, h1_nb_deces, 
     h1_budget_trimestriel, h1_nb_consultations),
    (h2_nom, h2_nb_lits, h2_nb_lits_occupes, h2_nb_medecins, 
     h2_population_zone, h2_nb_hospitalisations, h2_nb_deces, 
     h2_budget_trimestriel, h2_nb_consultations),
    (h3_nom, h3_nb_lits, h3_nb_lits_occupes, h3_nb_medecins, 
     h3_population_zone, h3_nb_hospitalisations, h3_nb_deces, 
     h3_budget_trimestriel, h3_nb_consultations),
    (h4_nom, h4_nb_lits, h4_nb_lits_occupes, h4_nb_medecins, 
     h4_population_zone, h4_nb_hospitalisations, h4_nb_deces, 
     h4_budget_trimestriel, h4_nb_consultations),
    (h5_nom, h5_nb_lits, h5_nb_lits_occupes, h5_nb_medecins, 
     h5_population_zone, h5_nb_hospitalisations, h5_nb_deces, 
     h5_budget_trimestriel, h5_nb_consultations)
]

# Calculer les KPIs pour tous les hopitaux
kpis_hopitaux = [calculer_kpis_hopital(*h) for h in hopitaux]

# Calcul des KPIs globaux
total_medecins = sum([h[3] for h in hopitaux])
total_population = sum([h[4] for h in hopitaux])
densite_nationale = (total_medecins / total_population) * 1000 if total_population > 0 else 0

taux_occupation_moyen = sum([k['taux_occupation'] for k in kpis_hopitaux]) / len(kpis_hopitaux)

# Valeur totale du stock de medicaments
valeur_stock_total = (m1_quantite_disponible * m1_cout_unitaire +
                     m2_quantite_disponible * m2_cout_unitaire +
                     m3_quantite_disponible * m3_cout_unitaire +
                     m4_quantite_disponible * m4_cout_unitaire +
                     m5_quantite_disponible * m5_cout_unitaire)

# Identifier les hopitaux critiques
hopitaux_critiques = [k for k in kpis_hopitaux if k['est_critique']]

# ============================================================
# SECTION E : RAPPORT TEXTUEL INITIAL (S2)
# ============================================================

def afficher_rapport_initial():
    """Affiche le rapport initial du systeme de sante (S2)"""
    print('=' * 70)
    print('  RAPPORT INITIAL — SYSTEME DE SANTE CONGOLAIS')
    print('  Version S2 — Donnees brutes et KPIs de base')
    print('=' * 70)
    print()
    
    print('  CONSTANTES NATIONALES')
    print('  ' + '-' * 50)
    print(f'  Taux EUR/FCFA : {TAUX_EUR_FCFA:.3f}')
    print(f'  Taux USD/FCFA : {TAUX_USD_FCFA:.1f}')
    print(f'  Norme OMS densite medicale : {SEUIL_OMS_DENSITE_MEDICALE}')
    print(f'  Norme OMS couverture vaccinale : {SEUIL_OMS_COUVERTURE_VACCIN}%')
    print(f'  Seuil alerte mortalite : {SEUIL_MORTALITE_ALERTE}%')
    print()
    
    print('  INDICATEURS GLOBAUX')
    print('  ' + '-' * 50)
    print(f'  Densite medicale nationale : {densite_nationale:.2f} medecins/1000 hab')
    print(f'  Taux occupation moyen : {taux_occupation_moyen:.1f}%')
    print(f'  Valeur stock total : {valeur_stock_total:,.0f} FCFA'.replace(',', ' '))
    print()

# ============================================================
# SECTION F : CLASSIFICATION STATUT STOCKS (S3)
# ============================================================

def classer_statut_stock(quantite, seuil):
    """
    Classifie le statut d'un medicament selon son stock
    
    Args:
        quantite: Quantite disponible
        seuil: Seuil de rupture
    
    Returns:
        dict: Statut, couleur, action
    """
    if quantite <= seuil:
        return {
            'statut': 'RUPTURE CRITIQUE',
            'couleur': '[ROUGE]',
            'action': 'Alerte immediate PNA — commande express sous 24h'
        }
    elif quantite <= seuil * 1.5:
        return {
            'statut': 'ALERTE STOCK',
            'couleur': '[ORANGE]',
            'action': 'Commande urgente a declencher sous 72h'
        }
    elif quantite <= seuil * 2.0:
        return {
            'statut': 'STOCK LIMITE',
            'couleur': '[JAUNE]',
            'action': 'Surveillance renforcee — planifier commande'
        }
    else:
        return {
            'statut': 'STOCK NORMAL',
            'couleur': '[VERT]',
            'action': 'Situation normale — suivi standard'
        }

# Classification des 5 medicaments
m1_class = classer_statut_stock(m1_quantite_disponible, m1_seuil_rupture)
m2_class = classer_statut_stock(m2_quantite_disponible, m2_seuil_rupture)
m3_class = classer_statut_stock(m3_quantite_disponible, m3_seuil_rupture)
m4_class = classer_statut_stock(m4_quantite_disponible, m4_seuil_rupture)
m5_class = classer_statut_stock(m5_quantite_disponible, m5_seuil_rupture)

# Compteurs de stocks
nb_ruptures_critiques = 0
nb_alertes_stock = 0
nb_stocks_limite = 0
nb_stocks_normaux = 0

if m1_class['statut'] == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m1_class['statut'] == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m1_class['statut'] == 'STOCK LIMITE':
    nb_stocks_limite += 1
else:
    nb_stocks_normaux += 1

if m2_class['statut'] == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m2_class['statut'] == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m2_class['statut'] == 'STOCK LIMITE':
    nb_stocks_limite += 1
else:
    nb_stocks_normaux += 1

if m3_class['statut'] == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m3_class['statut'] == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m3_class['statut'] == 'STOCK LIMITE':
    nb_stocks_limite += 1
else:
    nb_stocks_normaux += 1

if m4_class['statut'] == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m4_class['statut'] == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m4_class['statut'] == 'STOCK LIMITE':
    nb_stocks_limite += 1
else:
    nb_stocks_normaux += 1

if m5_class['statut'] == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m5_class['statut'] == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m5_class['statut'] == 'STOCK LIMITE':
    nb_stocks_limite += 1
else:
    nb_stocks_normaux += 1

# ============================================================
# SECTION G : CLASSIFICATION OCCUPATION HOPITAUX (S3)
# ============================================================

def classer_occupation(taux_occupation):
    """
    Classifie le niveau d'occupation d'un hopital
    
    Args:
        taux_occupation: Taux d'occupation en %
    
    Returns:
        dict: Niveau, couleur, interpretation
    """
    if taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
        return {
            'niveau': 'CRITIQUE',
            'couleur': '[ROUGE]',
            'interpretation': 'Surcharge critique des lits'
        }
    elif taux_occupation > SEUIL_OCCUPATION_ALERTE:
        return {
            'niveau': 'ALERTE',
            'couleur': '[ORANGE]',
            'interpretation': 'Surcharge des lits'
        }
    elif SEUIL_OCCUPATION_OPTIMAL_MIN <= taux_occupation <= SEUIL_OCCUPATION_OPTIMAL_MAX:
        return {
            'niveau': 'OPTIMAL',
            'couleur': '[VERT]',
            'interpretation': 'Taux d\'occupation optimal'
        }
    else:
        return {
            'niveau': 'SOUS-UTILISE',
            'couleur': '[JAUNE]',
            'interpretation': 'Sous-utilisation des lits'
        }

# Calcul des taux d'occupation
taux_occ_h1 = (h1_nb_lits_occupes / h1_nb_lits) * 100 if h1_nb_lits > 0 else 0
taux_occ_h2 = (h2_nb_lits_occupes / h2_nb_lits) * 100 if h2_nb_lits > 0 else 0
taux_occ_h3 = (h3_nb_lits_occupes / h3_nb_lits) * 100 if h3_nb_lits > 0 else 0
taux_occ_h4 = (h4_nb_lits_occupes / h4_nb_lits) * 100 if h4_nb_lits > 0 else 0
taux_occ_h5 = (h5_nb_lits_occupes / h5_nb_lits) * 100 if h5_nb_lits > 0 else 0

# Classification
occ_h1 = classer_occupation(taux_occ_h1)
occ_h2 = classer_occupation(taux_occ_h2)
occ_h3 = classer_occupation(taux_occ_h3)
occ_h4 = classer_occupation(taux_occ_h4)
occ_h5 = classer_occupation(taux_occ_h5)

# Compteurs d'occupation
nb_hopitaux_critiques = 0
nb_hopitaux_alerte = 0
nb_hopitaux_optimal = 0
nb_hopitaux_sous_utilises = 0

for occ in [occ_h1, occ_h2, occ_h3, occ_h4, occ_h5]:
    if occ['niveau'] == 'CRITIQUE':
        nb_hopitaux_critiques += 1
    elif occ['niveau'] == 'ALERTE':
        nb_hopitaux_alerte += 1
    elif occ['niveau'] == 'OPTIMAL':
        nb_hopitaux_optimal += 1
    else:
        nb_hopitaux_sous_utilises += 1

# ============================================================
# SECTION H : CLASSIFICATION COUVERTURE VACCINALE (S3)
# ============================================================

# Donnees des 4 departements
departements_vaccin = [
    {'nom': 'Brazzaville', 'population_cible': 450000, 'personnes_vaccinees': 418500},
    {'nom': 'Pointe-Noire', 'population_cible': 280000, 'personnes_vaccinees': 229600},
    {'nom': 'Pool', 'population_cible': 120000, 'personnes_vaccinees': 54000},
    {'nom': 'Sangha', 'population_cible': 85000, 'personnes_vaccinees': 35700},
]

def classer_couverture_vaccinale(taux):
    """
    Classifie la couverture vaccinale selon les normes OMS
    
    Args:
        taux: Taux de couverture en %
    
    Returns:
        dict: Statut, couleur, interpretation
    """
    if taux < SEUIL_CRITIQUE_COUVERTURE:
        return {
            'statut': 'ZONE CRITIQUE',
            'couleur': '[ROUGE]',
            'interpretation': f'Couverture < {SEUIL_CRITIQUE_COUVERTURE}% — Action urgente'
        }
    elif taux < SEUIL_RISQUE_COUVERTURE:
        return {
            'statut': 'ZONE A RISQUE',
            'couleur': '[ORANGE]',
            'interpretation': f'Couverture entre {SEUIL_CRITIQUE_COUVERTURE}% et {SEUIL_RISQUE_COUVERTURE}% — Surveillance renforcee'
        }
    elif taux < SEUIL_OMS_COUVERTURE_VACCIN:
        return {
            'statut': 'ZONE INSUFFISANTE',
            'couleur': '[JAUNE]',
            'interpretation': f'Couverture < {SEUIL_OMS_COUVERTURE_VACCIN}% — Intensifier la vaccination'
        }
    else:
        return {
            'statut': 'COUVERTURE OPTIMALE',
            'couleur': '[VERT]',
            'interpretation': f'Couverture >= {SEUIL_OMS_COUVERTURE_VACCIN}% — Conforme OMS'
        }

# Calcul et classification pour chaque departement
vaccin_departements = []
for dept in departements_vaccin:
    taux = (dept['personnes_vaccinees'] / dept['population_cible']) * 100 if dept['population_cible'] > 0 else 0
    classification = classer_couverture_vaccinale(taux)
    vaccin_departements.append({
        'nom': dept['nom'],
        'taux': round(taux, 1),
        'population_cible': dept['population_cible'],
        'personnes_vaccinees': dept['personnes_vaccinees'],
        'statut': classification['statut'],
        'couleur': classification['couleur'],
        'interpretation': classification['interpretation']
    })

# Compteurs de couverture vaccinale
nb_zones_critiques = 0
nb_zones_risque = 0
nb_zones_insuffisantes = 0
nb_zones_optimales = 0

for dept in vaccin_departements:
    if dept['statut'] == 'ZONE CRITIQUE':
        nb_zones_critiques += 1
    elif dept['statut'] == 'ZONE A RISQUE':
        nb_zones_risque += 1
    elif dept['statut'] == 'ZONE INSUFFISANTE':
        nb_zones_insuffisantes += 1
    else:
        nb_zones_optimales += 1

# ============================================================
# SECTION I : RAPPORT D'ETAT GLOBAL AVEC ALERTES (S3)
# ============================================================

def afficher_rapport_complet():
    """Affiche le rapport complet avec toutes les classifications S3"""
    
    print('=' * 80)
    print('  RAPPORT D\'ETAT SANITAIRE — CONGO-BRAZZAVILLE')
    print('  Version S3 — Classification automatique et alertes')
    print(f'  Date : 25 juin 2026 | Heure : {__import__("datetime").datetime.now().strftime("%H:%M")}')
    print('=' * 80)
    print()
    
    # SECTION F : Classification des stocks
    print('  SECTION F — CLASSIFICATION DES STOCKS MEDICAMENTS')
    print('  ' + '-' * 60)
    
    for nom, quantite, seuil, classif in [
        (m1_nom, m1_quantite_disponible, m1_seuil_rupture, m1_class),
        (m2_nom, m2_quantite_disponible, m2_seuil_rupture, m2_class),
        (m3_nom, m3_quantite_disponible, m3_seuil_rupture, m3_class),
        (m4_nom, m4_quantite_disponible, m4_seuil_rupture, m4_class),
        (m5_nom, m5_quantite_disponible, m5_seuil_rupture, m5_class),
    ]:
        print(f'  {classif["couleur"]} {nom}')
        print(f'      Stock : {quantite} unites | Seuil : {seuil}')
        print(f'      Statut : {classif["statut"]}')
        print(f'      Action : {classif["action"]}')
        print()
    
    print(f'  BILAN STOCKS :')
    print(f'      Ruptures critiques : {nb_ruptures_critiques}')
    print(f'      Alertes stock      : {nb_alertes_stock}')
    print(f'      Stocks limites     : {nb_stocks_limite}')
    print(f'      Stocks normaux     : {nb_stocks_normaux}')
    print('  ' + '-' * 60)
    print()
    
    # SECTION G : Classification des hopitaux
    print('  SECTION G — CLASSIFICATION DES HOPITAUX')
    print('  ' + '-' * 60)
    
    hopitaux_occupation = [
        (h1_nom, h1_nb_lits, h1_nb_lits_occupes, taux_occ_h1, occ_h1),
        (h2_nom, h2_nb_lits, h2_nb_lits_occupes, taux_occ_h2, occ_h2),
        (h3_nom, h3_nb_lits, h3_nb_lits_occupes, taux_occ_h3, occ_h3),
        (h4_nom, h4_nb_lits, h4_nb_lits_occupes, taux_occ_h4, occ_h4),
        (h5_nom, h5_nb_lits, h5_nb_lits_occupes, taux_occ_h5, occ_h5),
    ]
    
    for nom, lits_total, lits_occupes, taux, classif in hopitaux_occupation:
        print(f'  {classif["couleur"]} {nom}')
        print(f'      Lits : {lits_occupes}/{lits_total} occupes ({taux:.1f}%)')
        print(f'      Niveau : {classif["niveau"]}')
        print(f'      Interpretation : {classif["interpretation"]}')
        print()
    
    print(f'  BILAN OCCUPATION :')
    print(f'      Hopitaux en surcharge critique : {nb_hopitaux_critiques}')
    print(f'      Hopitaux en alerte             : {nb_hopitaux_alerte}')
    print(f'      Hopitaux optimaux              : {nb_hopitaux_optimal}')
    print(f'      Hopitaux sous-utilises         : {nb_hopitaux_sous_utilises}')
    print('  ' + '-' * 60)
    print()
    
    # SECTION H : Classification de la couverture vaccinale
    print('  SECTION H — COUVERTURE VACCINALE PAR DEPARTEMENT')
    print('  ' + '-' * 60)
    
    for dept in vaccin_departements:
        print(f'  {dept["couleur"]} {dept["nom"]}')
        print(f'      Population cible : {dept["population_cible"]:,}'.replace(',', ' '))
        print(f'      Vaccines         : {dept["personnes_vaccinees"]:,}'.replace(',', ' '))
        print(f'      Taux couverture  : {dept["taux"]:.1f}%')
        print(f'      Statut           : {dept["statut"]}')
        print(f'      {dept["interpretation"]}')
        print()
    
    print(f'  BILAN VACCINAL :')
    print(f'      Zones critiques       : {nb_zones_critiques}')
    print(f'      Zones a risque        : {nb_zones_risque}')
    print(f'      Zones insuffisantes   : {nb_zones_insuffisantes}')
    print(f'      Zones optimales       : {nb_zones_optimales}')
    print('  ' + '-' * 60)
    print()
    
    # SECTION I : Resume executif
    print('  SECTION I — RESUME EXECUTIF ET ALERTES')
    print('  ' + '-' * 60)
    
    # Alertes globales
    alertes_actives = []
    
    if nb_ruptures_critiques > 0:
        alertes_actives.append(f'{nb_ruptures_critiques} medicaments en RUPTURE CRITIQUE')
    if nb_alertes_stock > 0:
        alertes_actives.append(f'{nb_alertes_stock} medicaments en ALERTE STOCK')
    if nb_hopitaux_critiques > 0:
        alertes_actives.append(f'{nb_hopitaux_critiques} hopitaux en SURCHARGE CRITIQUE')
    if nb_zones_critiques > 0:
        alertes_actives.append(f'{nb_zones_critiques} departements en ZONE CRITIQUE (vaccination)')
    
    if alertes_actives:
        print('  !! ALERTES ACTIVES :')
        for alerte in alertes_actives:
            print(f'      • {alerte}')
    else:
        print('  ✓ Aucune alerte active — situation satisfaisante')
    
    print()
    
    # Recommandations
    print('  RECOMMANDATIONS PRIORITAIRES :')
    if nb_ruptures_critiques >= 2 or nb_hopitaux_critiques >= 3:
        print('      . Mobiliser la reserve nationale PNA')
        print('      → Activer le plan d\'urgence national')
        print('      → Deployment d\'equipes mobiles')
    elif nb_ruptures_critiques >= 1 or nb_zones_critiques >= 1:
        print('      . Renforcer les actions dans les zones critiques')
        print('      → Prioriser les hopitaux avec ruptures')
        print('      → Intensifier les campagnes de vaccination')
    else:
        print('      . Maintenir le suivi standard')
        print('      → Surveillance continue des indicateurs')
    
    print('  ' + '-' * 60)
    print()
    
    # Indicateurs globaux
    print('  INDICATEURS GLOBAUX :')
    print(f'      Densite medicale nationale : {densite_nationale:.2f} medecins/1000 hab')
    print(f'      Taux occupation moyen      : {taux_occupation_moyen:.1f}%')
    print(f'      Valeur stock total         : {valeur_stock_total:,.0f} FCFA'.replace(',', ' '))
    print(f'      Ruptures nationales        : {nb_ruptures_critiques}')
    print(f'      Alertes nationales         : {nb_alertes_stock}')
    
    print()
    print('=' * 80)
    print('  FIN DU RAPPORT D\'ETAT SANITAIRE')
    print('=' * 80)

# ============================================================
# EXECUTION PRINCIPALE
# ============================================================

if __name__ == "__main__":
    # Afficher le rapport initial (S2)
    afficher_rapport_initial()
    
    # Afficher le rapport complet (S3)
    afficher_rapport_complet()