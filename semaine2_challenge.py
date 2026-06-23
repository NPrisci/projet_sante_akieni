# ============================================================ 
# CHALLENGE ENTREPRISE — Rapport comparatif departement Pool 
# ============================================================ 

# === CONSTANTES (definies AVANT toute utilisation) ===
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants
SEUIL_MORTALITE_ALERTE = 2.0        # % deces/hospitalisations
SEUIL_CRITIQUE_DENSITE = 0.05       # medecins/1000 hab
COUT_MEDECIN_TRIMESTRE = 1_200_000.0  # FCFA

# === DONNEES DES 3 HOPITAUX DU POOL ===

# Hopital 1 - Hopital District Kinkala
h1_nom = 'Hopital District Kinkala'
h1_budget = 12_500_000.0  # float - budget en FCFA
h1_consultations = 1_847   # int - consultations externes
h1_hospitalisations = 312  # int - hospitalisations
h1_deces = 8              # int - deces hospitaliers
h1_lits_totaux = 45       # int - lits totaux
h1_lits_occupes = 41      # int - lits occupes
h1_medecins = 3           # int - medecins permanents
h1_population = 85_000    # int - population desservie

# Hopital 2 - CMS de Vindza
h2_nom = 'CMS de Vindza'
h2_budget = 6_800_000.0
h2_consultations = 923
h2_hospitalisations = 87
h2_deces = 2
h2_lits_totaux = 20
h2_lits_occupes = 14
h2_medecins = 1
h2_population = 42_000

# Hopital 3 - Hopital de Kindamba
h3_nom = 'Hopital de Kindamba'
h3_budget = 9_200_000.0
h3_consultations = 1_234
h3_hospitalisations = 201
h3_deces = 11
h3_lits_totaux = 35
h3_lits_occupes = 33
h3_medecins = 2
h3_population = 67_000

# === FONCTIONS DE CALCUL ===

def calculer_kpis_hopital(nom, budget, consultations, hospitalisations, 
                          deces, lits_totaux, lits_occupes, 
                          medecins, population):
    """
    Calcule les KPIs pour un hopital du Pool
    
    Returns:
        dict: Dictionnaire contenant tous les indicateurs
    """
    # Cout moyen par patient (en FCFA)
    if consultations > 0:
        cout_moyen = budget / consultations
    else:
        cout_moyen = 0.0
    
    # Taux d'occupation des lits (%)
    if lits_totaux > 0:
        taux_occupation = (lits_occupes / lits_totaux) * 100
    else:
        taux_occupation = 0.0
    
    # Densite medicale (medecins pour 1000 habitants)
    if population > 0:
        densite_medicale = (medecins / population) * 1000
    else:
        densite_medicale = 0.0
    
    # Taux de mortalite hospitaliere (%)
    if hospitalisations > 0:
        taux_mortalite = (deces / hospitalisations) * 100
    else:
        taux_mortalite = 0.0
    
    # Est-ce que l'hopital est en situation critique?
    est_critique = (taux_mortalite > SEUIL_MORTALITE_ALERTE or 
                   densite_medicale < SEUIL_CRITIQUE_DENSITE)
    
    # Raison de la criticite
    raisons_critiques = []
    if taux_mortalite > SEUIL_MORTALITE_ALERTE:
        raisons_critiques.append(f"Mortalite elevee ({taux_mortalite:.1f}% > {SEUIL_MORTALITE_ALERTE}%)")
    if densite_medicale < SEUIL_CRITIQUE_DENSITE:
        raisons_critiques.append(f"Densite medicale critique ({densite_medicale:.2f} < {SEUIL_CRITIQUE_DENSITE})")
    
    return {
        'nom': nom,
        'cout_moyen': round(cout_moyen, 0),
        'taux_occupation': round(taux_occupation, 1),
        'densite_medicale': round(densite_medicale, 2),
        'taux_mortalite': round(taux_mortalite, 1),
        'est_critique': est_critique,
        'raisons_critiques': raisons_critiques,
        'medecins': medecins,
        'consultations': consultations,
        'deces': deces
    }

# === CALCULS ===

# Calcul des KPIs pour chaque hopital
kpi_h1 = calculer_kpis_hopital(h1_nom, h1_budget, h1_consultations, 
                                h1_hospitalisations, h1_deces, 
                                h1_lits_totaux, h1_lits_occupes, 
                                h1_medecins, h1_population)

kpi_h2 = calculer_kpis_hopital(h2_nom, h2_budget, h2_consultations, 
                                h2_hospitalisations, h2_deces, 
                                h2_lits_totaux, h2_lits_occupes, 
                                h2_medecins, h2_population)

kpi_h3 = calculer_kpis_hopital(h3_nom, h3_budget, h3_consultations, 
                                h3_hospitalisations, h3_deces, 
                                h3_lits_totaux, h3_lits_occupes, 
                                h3_medecins, h3_population)

# Liste des KPIs pour traitement
kpis_pool = [kpi_h1, kpi_h2, kpi_h3]

# Calcul du budget total pour 5 medecins (BONUS)
budget_total = h1_budget + h2_budget + h3_budget
cout_5_medecins = COUT_MEDECIN_TRIMESTRE * 5
budget_suffisant = budget_total >= cout_5_medecins

# === AFFICHAGE DU RAPPORT ===

def afficher_rapport_pool():
    """Affiche le rapport comparatif pour le departement du Pool"""
    
    print("="*70)
    print("  RAPPORT COMPARATIF URBAIN - DEPARTEMENT DU POOL")
    print("  A l'attention du Dr. ELENGA Pascal, DSS")
    print("  Date: 8 janvier 2026")
    print("="*70)
    print()
    
    # En-tete du tableau
    print("TABLEAU DE BORD - 3 HOPITAUX DU POOL")
    print("-"*70)
    print(f"{'HOPITAL':<25} {'COUT MOYEN':>15} {'Taux occ.':>10} {'Densite':>10} {'Mortalite':>10} {'STATUS':>12}")
    print(f"{'':25} {'(FCFA/pat)':>15} {'(%)':>10} {'(/1000 hab)':>10} {'(%)':>10} {'':12}")
    print("-"*70)
    
    # Lignes du tableau
    for k in kpis_pool:
        status = "CRITIQUE" if k['est_critique'] else "OK"
        # Formatage avec espaces pour les nombres
        cout_formate = f"{k['cout_moyen']:,.0f}".replace(',', ' ')
        print(f"{k['nom']:<25} "
              f"{cout_formate:>15} "
              f"{k['taux_occupation']:>10.1f} "
              f"{k['densite_medicale']:>10.2f} "
              f"{k['taux_mortalite']:>10.1f} "
              f"{status:>12}")
    
    print("-"*70)
    print()
    
    # Analyse detaillee
    print("ANALYSE DETAILLEE")
    print("-"*70)
    
    # Identifier l'hopital critique
    hopitaux_critiques = [k for k in kpis_pool if k['est_critique']]
    
    if hopitaux_critiques:
        print("ALERTE - Hopitaux en situation critique identifies:")
        for k in hopitaux_critiques:
            print(f"  * {k['nom']}:")
            for raison in k['raisons_critiques']:
                print(f"    - {raison}")
    else:
        print("Aucun hopital en situation critique dans le departement du Pool")
    print()
    
    # Comparaison avec les normes OMS
    print("COMPARAISON AUX NORMES OMS:")
    print("-"*70)
    
    # Densite medicale moyenne du Pool
    densite_moyenne = sum([k['densite_medicale'] for k in kpis_pool]) / len(kpis_pool)
    print(f"Densite medicale moyenne du Pool: {densite_moyenne:.2f} medecins/1000 hab")
    print(f"  Norme OMS: {SEUIL_OMS_DENSITE_MEDICALE} medecins/1000 hab")
    if densite_moyenne >= SEUIL_OMS_DENSITE_MEDICALE:
        print("  Conforme aux normes OMS")
    else:
        print("  EN DESSOUS DES NORMES OMS")
    print()
    
    # Taux d'occupation moyen du Pool
    occ_moyenne = sum([k['taux_occupation'] for k in kpis_pool]) / len(kpis_pool)
    print(f"Taux d'occupation moyen du Pool: {occ_moyenne:.1f}%")
    print("  Optimal OMS: 70-85%")
    if 70 <= occ_moyenne <= 85:
        print("  Dans la zone optimale")
    elif occ_moyenne < 70:
        print("  Sous-utilisation des lits")
    else:
        print("  SURCHARGE DES LITS (>85%)")
    print()
    
    # Moyenne des couts
    cout_moyen_pool = sum([k['cout_moyen'] for k in kpis_pool]) / len(kpis_pool)
    print(f"Cout moyen par patient dans le Pool: {cout_moyen_pool:,.0f} FCFA".replace(',', ' '))
    print()
    
    # --- BONUS : Budget pour 5 medecins ---
    print("BONUS - ANALYSE BUDGETAIRE")
    print("-"*70)
    print(f"Budget total des 3 hopitaux: {budget_total:,.0f} FCFA".replace(',', ' '))
    print(f"Cout pour recruter 5 medecins (trimestriel): {cout_5_medecins:,.0f} FCFA".replace(',', ' '))
    print(f"Budget restant apres recrutement: {budget_total - cout_5_medecins:,.0f} FCFA".replace(',', ' '))
    
    if budget_suffisant:
        print("Le budget total est SUFFISANT pour recruter 5 medecins")
        print(f"  Marge de manoeuvre: {(budget_total - cout_5_medecins):,.0f} FCFA".replace(',', ' '))
    else:
        deficit = cout_5_medecins - budget_total
        print("Le budget total est INSUFFISANT pour recruter 5 medecins")
        print(f"  Deficit: {deficit:,.0f} FCFA".replace(',', ' '))
    
    # Recommandations
    print()
    print("RECOMMANDATIONS")
    print("-"*70)
    print("1. Renforcer le personnel medical dans les structures critiques")
    print("2. Prioriser les hopitaux avec une densite medicale < 0.05")
    print("3. Mettre en place un systeme de surveillance de la mortalite")
    print("4. Optimiser l'utilisation des lits dans les hopitaux en surcharge")
    
    print("="*70)
    print("FIN DU RAPPORT - A TRANSMETTRE AU MINISTRE")
    print("="*70)

# === EXECUTION ===
if __name__ == "__main__":
    afficher_rapport_pool()