# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS 
# ============================================================ 
 
# --- DONNEES BRUTES --- 
budget_fcfa          = 87_450_000   # underscore pour lisibilite des grands nombres 
nb_consultations_ext = 4823 
nb_hospitalisations  = 1247 
nb_deces             = 18 
nb_lits_total        = 180 
nb_lits_occupes      = 143 
nb_medecins          = 22 
nb_infirmiers        = 58 
population_dept      = 128_000 
taux_eur_fcfa        = 655.957 
taux_usd_fcfa        = 600.0 
 
# --- A COMPLETER --- 
# 1. Conversions devises 
budget_eur = budget_fcfa / taux_eur_fcfa  # 87_450_000 / 655.957
budget_usd = budget_fcfa / taux_usd_fcfa  # 87_450_000 / 600.0
 
# Arrondi à 2 décimales 
budget_eur = round(budget_eur, 2)
budget_usd = round(budget_usd, 2)
 
# 2. Indicateurs OMS 
densite_medicale     = (nb_medecins / population_dept) * 1000  # médecins pour 1000 hab
taux_mortalite       = (nb_deces / nb_hospitalisations) * 100   # en pourcentage
taux_occupation      = (nb_lits_occupes / nb_lits_total) * 100  # en pourcentage
 
# Arrondi à 1 décimale pour l'affichage
densite_medicale = round(densite_medicale, 1)
taux_mortalite = round(taux_mortalite, 1)
taux_occupation = round(taux_occupation, 1)
 
# 3. Division entiere et modulo 
budget_medicaments   = int(budget_fcfa * 0.35)  # 30_607_500 FCFA
cout_journalier_meds = 450_000 
jours_stock          = budget_medicaments // cout_journalier_meds   # division entiere = 68 jours
jours_restants       = budget_medicaments % cout_journalier_meds    # modulo = reste
 
# 4. Puissance pour projection 
budget_n_plus_2      = budget_fcfa * (1.08 ** 2)   # croissance 8% sur 2 ans
budget_n_plus_2 = round(budget_n_plus_2, 1)  # arrondi à 1 décimale
 
# 5. Pair ou impair (consultations)
est_pair = nb_consultations_ext % 2 == 0  # 4823 % 2 = 1 => impair
 
# --- AFFICHAGE RAPPORT --- 
print(f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===\n')
 
# Budget
print(f'### BUDGET ###')
print(f'Depenses Q4: {budget_fcfa:,} FCFA'.replace(',', ' '))
print(f'En euros: {budget_eur:,.2f} EUR'.replace(',', ' '))
print(f'En dollars: {budget_usd:,.2f} USD'.replace(',', ' '))
print()
 
# Indicateurs OMS
print(f'### INDICATEURS OMS ###')
print(f'Densite medicale: {densite_medicale} medecins / 1000 hab [Norme OMS: >= 2.3]')
print(f'Taux mortalite: {taux_mortalite}% [Seuil alerte: > 2%]')
print(f'Taux occupation: {taux_occupation}% [Optimal: 70-85%]')
print()
 
# Analyse pharmacie
print(f'### ANALYSE PHARMACIE ###')
print(f'Budget medicaments: {budget_medicaments:,} FCFA'.replace(',', ' '))
print(f'Jours de stock: {jours_stock} jours')
print(f'Jours depassement: {jours_restants} jours')
print()
 
# Projection
print(f'### PROJECTION ###')
print(f'Budget N+2 (8%/an): {budget_n_plus_2:,.1f} FCFA'.replace(',', ' '))
 
# Alertes
if densite_medicale < 2.3:
    print(f'ALERTE: Densite medicale CRITIQUE ({densite_medicale} pour 1000 hab - norme OMS: 2.3)')
 
if taux_mortalite > 2:
    print(f'ALERTE: Taux de mortalite eleve ({taux_mortalite}% - seuil: 2%)')
 
print()
print(f'### INFORMATIONS SUPPLEMENTAIRES ###')
print(f'Nombre de consultations externes: {nb_consultations_ext} patients')
print(f'Pair ou impair: {"PAIR" if est_pair else "IMPAIR"} (utile pour rapports bi-mensuels)')
print(f'Budget medicaments = 35% du budget total: {budget_medicaments:,} FCFA'.replace(',', ' '))