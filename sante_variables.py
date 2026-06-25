# ============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# ============================================================ 

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 

# Taux de change
TAUX_EUR_FCFA = 655.957  # Taux fixe CFA
TAUX_USD_FCFA = 600.0    # Taux approximatif 2025

# Seuils OMS (en MAJUSCULES selon convention Python)
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations
SEUIL_CRITIQUE_DENSITE = 0.05       # Densite critique pour alerte
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock

# 12 departements officiels du Congo
DEPARTEMENTS_CONGO = [
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# === SECTION B : VARIABLES DES 5 HOPITAUX =================== 

# Hopital 1 — CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
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
h3_nb_lits = 120
h3_nb_lits_occupes = 85
h3_nb_medecins = 15
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
h4_nb_lits = 65
h4_nb_lits_occupes = 48
h4_nb_medecins = 8
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
h5_nb_lits = 30
h5_nb_lits_occupes = 22
h5_nb_medecins = 3
h5_nb_infirmiers = 15
h5_population_zone = 35_000
h5_budget_trimestriel = 8_200_000.0
h5_nb_consultations = 678
h5_nb_hospitalisations = 189
h5_nb_deces = 5
h5_taux_remise_cnss = 15.0

# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================ 

# Medicament 1 — Antipaludique
med1_nom = 'Artemether-Lumefantrine'
med1_categorie = 'Antipaludique'
med1_quantite_disponible = 12_500  # unites
med1_seuil_rupture = 500  # unites
med1_cout_unitaire = 1_500.0  # FCFA
med1_duree_stock_jours = 68

# Medicament 2 — Antibiotique
med2_nom = 'Amoxicilline'
med2_categorie = 'Antibiotique'
med2_quantite_disponible = 8_200
med2_seuil_rupture = 1_000
med2_cout_unitaire = 450.0
med2_duree_stock_jours = 45

# Medicament 3 — Antalgique
med3_nom = 'Paracetamol'
med3_categorie = 'Antalgique'
med3_quantite_disponible = 15_000
med3_seuil_rupture = 2_000
med3_cout_unitaire = 150.0
med3_duree_stock_jours = 30

# Medicament 4 — SRO (Soluté de Réhydratation Orale)
med4_nom = 'SRO (Soluté de Réhydratation Orale)'
med4_categorie = 'Réhydratation'
med4_quantite_disponible = 3_500
med4_seuil_rupture = 300
med4_cout_unitaire = 200.0
med4_duree_stock_jours = 25

# Medicament 5 — Vaccin
med5_nom = 'Vaccin antipaludique RTS,S'
med5_categorie = 'Vaccin'
med5_quantite_disponible = 2_000
med5_seuil_rupture = 100
med5_cout_unitaire = 8_500.0
med5_duree_stock_jours = 40

# === SECTION D : CALCULS D'INITIALISATION =================== 

# Calcul des KPIs pour chaque hopital
def calculer_kpis_hopital(nom, nb_lits, nb_lits_occupes, nb_medecins, 
                          population_zone, nb_hospitalisations, nb_deces, 
                          budget_trimestriel, nb_consultations):
    """
    Calcule les indicateurs clés pour un hopital
    
    Returns:
        dict: Dictionnaire contenant tous les KPIs
    """
    # Densité médicale (médecins pour 1000 habitants)
    densite_medicale = (nb_medecins / population_zone) * 1000
    
    # Taux d'occupation des lits (%)
    taux_occupation = (nb_lits_occupes / nb_lits) * 100
    
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
densite_nationale = (total_medecins / total_population) * 1000

taux_occupation_moyen = sum([k['taux_occupation'] for k in kpis_hopitaux]) / len(kpis_hopitaux)

# Valeur totale du stock de medicaments
valeur_stock_total = (med1_quantite_disponible * med1_cout_unitaire +
                     med2_quantite_disponible * med2_cout_unitaire +
                     med3_quantite_disponible * med3_cout_unitaire +
                     med4_quantite_disponible * med4_cout_unitaire +
                     med5_quantite_disponible * med5_cout_unitaire)

# Identifier les hopitaux critiques
hopitaux_critiques = [k for k in kpis_hopitaux if k['est_critique']]

# === SECTION E : RAPPORT D'INVENTAIRE ======================= 

def afficher_rapport_inventaire():
    """Affiche le rapport complet d'inventaire du système de santé"""
    
    print("="*70)
    print("  RAPPORT D'INVENTAIRE — SYSTEME DE SANTE CONGOLAIS")
    print("  Date: 8 janvier 2026")
    print("="*70)
    print()
    
    # 1. CONSTANTES NATIONALES
    print("1. CONSTANTES NATIONALES ET NORMES OMS")
    print("-"*70)
    print(f"Taux de change EUR/FCFA: {TAUX_EUR_FCFA:.3f}")
    print(f"Taux de change USD/FCFA: {TAUX_USD_FCFA:.1f}")
    print(f"Seuil OMS densité médicale: {SEUIL_OMS_DENSITE_MEDICALE} médecins/1000 hab")
    print(f"Seuil OMS couverture vaccinale: {SEUIL_OMS_COUVERTURE_VACCIN}%")
    print(f"Seuil alerte mortalité: {SEUIL_MORTALITE_ALERTE}%")
    print(f"Seuil critique densité: {SEUIL_CRITIQUE_DENSITE} médecins/1000 hab")
    print(f"Nombre de départements: {len(DEPARTEMENTS_CONGO)}")
    print()
    
    # 2. INDICATEURS GLOBAUX
    print("2. INDICATEURS GLOBAUX")
    print("-"*70)
    print(f"Densité médicale nationale: {densite_nationale:.2f} médecins/1000 hab")
    print(f"  → {'✓ CONFORME' if densite_nationale >= SEUIL_OMS_DENSITE_MEDICALE else '⚠️ CRITIQUE'} (Norme OMS: {SEUIL_OMS_DENSITE_MEDICALE})")
    print(f"Taux d'occupation moyen: {taux_occupation_moyen:.1f}%")
    print(f"Valeur totale du stock: {valeur_stock_total:,.0f} FCFA".replace(',', ' '))
    print(f"  → {valeur_stock_total/TAUX_EUR_FCFA:,.2f} EUR".replace(',', ' '))
    print(f"  → {valeur_stock_total/TAUX_USD_FCFA:,.2f} USD".replace(',', ' '))
    print()
    
    # 3. DETAIL DES HOPITAUX
    print("3. DETAIL DES 5 HOPITAUX")
    print("-"*70)
    for i, k in enumerate(kpis_hopitaux, 1):
        print(f"[{i}] {k['nom']}")
        print(f"    • Densité médicale: {k['densite_medicale']} médecins/1000 hab")
        print(f"    • Taux d'occupation: {k['taux_occupation']}%")
        print(f"    • Taux de mortalité: {k['taux_mortalite']}%")
        print(f"    • Coût moyen/patient: {k['cout_moyen_patient']:,.0f} FCFA".replace(',', ' '))
        print(f"    • Médecins: {k['nb_medecins']} | Lits: {k['nb_lits']}")
        
        if k['est_critique']:
            print("STATUS: CRITIQUE")
            if k['taux_mortalite'] > SEUIL_MORTALITE_ALERTE:
                print(f"       → Mortalité élevée ({k['taux_mortalite']}% > {SEUIL_MORTALITE_ALERTE}%)")
            if k['densite_medicale'] < SEUIL_CRITIQUE_DENSITE:
                print(f"       → Densité médicale critique ({k['densite_medicale']} < {SEUIL_CRITIQUE_DENSITE})")
        else:
            print("    ✓ STATUS: OK")
        print()
    
    # 4. DETAIL DES MEDICAMENTS
    print("4. DETAIL DES MEDICAMENTS ESSENTIELS")
    print("-"*70)
    medicaments = [
        (med1_nom, med1_categorie, med1_quantite_disponible, med1_seuil_rupture, 
         med1_cout_unitaire, med1_duree_stock_jours),
        (med2_nom, med2_categorie, med2_quantite_disponible, med2_seuil_rupture, 
         med2_cout_unitaire, med2_duree_stock_jours),
        (med3_nom, med3_categorie, med3_quantite_disponible, med3_seuil_rupture, 
         med3_cout_unitaire, med3_duree_stock_jours),
        (med4_nom, med4_categorie, med4_quantite_disponible, med4_seuil_rupture, 
         med4_cout_unitaire, med4_duree_stock_jours),
        (med5_nom, med5_categorie, med5_quantite_disponible, med5_seuil_rupture, 
         med5_cout_unitaire, med5_duree_stock_jours)
    ]
    
    for i, med in enumerate(medicaments, 1):
        nom, categorie, qte, seuil, cout, jours = med
        est_rupture = qte < seuil
        print(f"[{i}] {nom} ({categorie})")
        print(f"    • Quantité: {qte:,} unités".replace(',', ' '))
        print(f"    • Seuil de rupture: {seuil:,} unités".replace(',', ' '))
        print(f"    • Coût unitaire: {cout:,.0f} FCFA".replace(',', ' '))
        print(f"    • Jours de stock: {jours} jours")
        if est_rupture:
            print(f"    ALERTE: STOCK CRITIQUE ({qte} < {seuil})")
        else:
            print(f"    ✓ Stock OK")
        print()
    
    # 5. SYNTHESE
    print("5. SYNTHESE ET ALERTES")
    print("-"*70)
    print(f"Nombre d'hopitaux critiques: {len(hopitaux_critiques)}")
    if hopitaux_critiques:
        print("Hopitaux en situation critique:")
        for h in hopitaux_critiques:
            print(f"  • {h['nom']}")
    else:
        print("✓ Aucun hopital en situation critique")
    
    print("="*70)
    print("FIN DU RAPPORT")
    print("="*70)

# Exécuter le rapport si le fichier est exécuté directement
if __name__ == "__main__":
    afficher_rapport_inventaire()