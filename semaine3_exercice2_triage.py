# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# ============================================================

from typing import Tuple, List, Optional

# --- SAISIE DES DONNEES PATIENT ---
print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()

nom_patient: str = input('Nom du patient : ')
age_patient: int = int(input('Age (annees) : '))
temperature: float = float(input('Temperature (degres C, ex: 38.4) : '))
spo2: float = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst: int = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur: int = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

print()
print('=' * 55)

# --- VALIDATION DES PLAGES ---
erreur_saisie: bool = False

if temperature < 35.0 or temperature > 43.0:
    print('ERREUR : Valeur de temperature impossible — verifier la saisie')
    erreur_saisie = True

if spo2 < 50.0 or spo2 > 100.0:
    print('ERREUR : SpO2 hors plage — verifier le capteur')
    erreur_saisie = True

if tension_syst < 50 or tension_syst > 250:
    print('ERREUR : Tension hors plage — verifier le brassard')
    erreur_saisie = True

if douleur < 0 or douleur > 10:
    print('ERREUR : Douleur doit etre entre 0 et 10')
    erreur_saisie = True

if age_patient < 0 or age_patient > 120:
    print('ERREUR : Age invalide — verifier la saisie')
    erreur_saisie = True

if erreur_saisie:
    print('\n=== TRIAGE ANNULE — VEUILLEZ RESSASIR LES DONNEES ===')
    print('=' * 55)
    exit()

# --- TRIAGE ---
niveau_triage: str
couleur_triage: str
delai_pec: str
action_triage: str
motif_principal: str

if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec = '0 minute'
    action_triage = 'Medecin present immediatement — code ROUGE active'
    
    motifs: List[str] = []
    if temperature > 39.5:
        motifs.append(f'Temperature {temperature} C > seuil 39.5 C')
    if spo2 < 90:
        motifs.append(f'SpO2 {spo2}% < seuil 90%')
    if tension_syst > 180:
        motifs.append(f'Tension {tension_syst} mmHg > seuil 180 mmHg')
    motif_principal = ' OU '.join(motifs)

elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
    niveau_triage = '2 — URGENT'
    couleur_triage = '[ORANGE]'
    delai_pec = '10 minutes'
    action_triage = 'Appel medecin senior — surveillance continue'
    
    motifs = []
    if temperature > 38.5:
        motifs.append(f'Temperature {temperature} C > seuil 38.5 C')
    if spo2 < 94:
        motifs.append(f'SpO2 {spo2}% < seuil 94%')
    if tension_syst > 140:
        motifs.append(f'Tension {tension_syst} mmHg > seuil 140 mmHg')
    motif_principal = ' OU '.join(motifs)

elif temperature > 37.5 or douleur > 6:
    niveau_triage = '3 — URGENT DIFFERE'
    couleur_triage = '[JAUNE]'
    delai_pec = '30 minutes'
    action_triage = 'Infirmier — surveillance et monitoring'
    
    motifs = []
    if temperature > 37.5:
        motifs.append(f'Temperature {temperature} C > seuil 37.5 C')
    if douleur > 6:
        motifs.append(f'Douleur {douleur}/10 > seuil 6')
    motif_principal = ' OU '.join(motifs)

else:
    niveau_triage = '4 — MOINS URGENT'
    couleur_triage = '[VERT]'
    delai_pec = '120 minutes'
    action_triage = 'File d\'attente standard'
    motif_principal = 'Tous les parametres sont dans les normes'

# --- DETERMINATION DU STATUT DES PARAMETRES ---
temp_statut: str
if temperature > 39.5:
    temp_statut = 'CRITIQUE (> 39.5)'
elif temperature > 38.5:
    temp_statut = 'ELEVEE (> 38.5)'
elif temperature > 37.5:
    temp_statut = 'LEGEREMENT ELEVEE (> 37.5)'
else:
    temp_statut = 'NORMAL'

spo2_statut: str
if spo2 < 90:
    spo2_statut = 'CRITIQUE (< 90%)'
elif spo2 < 94:
    spo2_statut = 'BAS (< 94%)'
else:
    spo2_statut = 'NORMAL'

tension_statut: str
if tension_syst > 180:
    tension_statut = 'CRITIQUE (> 180)'
elif tension_syst > 140:
    tension_statut = 'ELEVEE (> 140)'
else:
    tension_statut = 'NORMAL'

douleur_statut: str
if douleur > 6:
    douleur_statut = 'ELEVEE (> 6/10)'
else:
    douleur_statut = 'NORMAL'

# --- AFFICHAGE FICHE TRIAGE ---
print()
print('=' * 55)
print(f'  RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)
print()
print('  PARAMETRES VITAUX')
print('  ' + '-' * 50)
print(f'  Temperature     : {temperature:.1f} C        [{temp_statut}]')
print(f'  Saturation O2   : {spo2:.1f} %        [{spo2_statut}]')
print(f'  Tension systol. : {tension_syst} mmHg      [{tension_statut}]')
print(f'  Douleur         : {douleur} / 10        [{douleur_statut}]')
print(f'  Age             : {age_patient} ans')
print('  ' + '-' * 50)
print()
print(f'  NIVEAU DE TRIAGE : {niveau_triage}')
print(f'  COULEUR          : {couleur_triage}')
print(f'  PRISE EN CHARGE  : {delai_pec}')
print(f'  ACTION           : {action_triage}')
print()
print('  ' + '-' * 50)
print(f'  Motif principal  : {motif_principal}')
print('=' * 55)

if niveau_triage == '1 — IMMEDIAT':
    print('\n  !! ALERTE ROUGE — PATIENT CRITIQUE !!')
    print('  Equipe de reanimation prevenue')
    print('=' * 55)

# --- PROTOCOLE ---
print('\n' + '=' * 55)
print('  PROTOCOLE DE TRIAGE — RAPPEL')
print('=' * 55)
print('  Niveau 1 [ROUGE]  : Temperature > 39.5 OU SpO2 < 90 OU Tension > 180')
print('  Niveau 2 [ORANGE] : Temperature > 38.5 OU SpO2 < 94 OU Tension > 140')
print('  Niveau 3 [JAUNE]  : Temperature > 37.5 OU Douleur > 6')
print('  Niveau 4 [VERT]   : Tous les parametres sont normaux')
print('=' * 55)

# ============================================================
# BONUS : TESTS AUTOMATISES AVEC TYPE HINTS
# ============================================================

print('\n' + '=' * 55)
print('  BONUS : TESTS AUTOMATISES DU PROTOCOLE')
print('=' * 55)

def tester_triage(
    nom: str,
    temp: float,
    spo2_val: float,  
    tension: int,
    douleur_val: int,  
    age: int,
    attendu: str
) -> None:
    """
    Teste le triage pour un cas donne et verifie le resultat
    
    Args:
        nom: Nom du test
        temp: Temperature en degres Celsius
        spo2_val: Saturation en oxygène en %
        tension: Tension systolique en mmHg
        douleur_val: Niveau de douleur /10
        age: Age en annees
        attendu: Niveau de triage attendu
    """
    if temp > 39.5 or spo2_val < 90 or tension > 180:
        resultat = '1 — IMMEDIAT'
    elif temp > 38.5 or spo2_val < 94 or tension > 140:
        resultat = '2 — URGENT'
    elif temp > 37.5 or douleur_val > 6:
        resultat = '3 — URGENT DIFFERE'
    else:
        resultat = '4 — MOINS URGENT'
    
    ok: bool = resultat == attendu
    symbole: str = '✓' if ok else '✗'
    print(f'  {symbole} {nom}: {resultat} (Attendu: {attendu})')
    if not ok:
        print(f'      Temp={temp}, SpO2={spo2_val}, Tension={tension}, Douleur={douleur_val}')

# Liste des cas de test
cas_test: List[Tuple[str, float, float, int, int, int, str]] = [
    ('Cas 1 - ROUGE', 40.1, 97.0, 120, 3, 42, '1 — IMMEDIAT'),
    ('Cas 2 - ROUGE', 37.0, 88.0, 120, 2, 45, '1 — IMMEDIAT'),
    ('Cas 3 - ORANGE', 38.0, 96.0, 145, 4, 50, '2 — URGENT'),
    ('Cas 4 - JAUNE', 38.0, 95.5, 130, 7, 35, '3 — URGENT DIFFERE'),
    ('Cas 5 - VERT', 36.8, 98.0, 125, 2, 28, '4 — MOINS URGENT'),
    ('Cas limite - VERT', 39.5, 90.0, 180, 6, 60, '4 — MOINS URGENT'),
]

print('\n  Execution des tests...')
print('  ' + '-' * 50)
for test in cas_test:
    tester_triage(*test)
print('  ' + '-' * 50)
print('  Tests termines')

print('\n' + '=' * 55)
print('  FIN DU SYSTEME DE TRIAGE')
print('=' * 55)