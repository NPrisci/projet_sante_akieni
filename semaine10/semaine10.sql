-- ============================================================
-- PROJET FIL ROUGE SQL - Semaine 10
-- Ligue Communale de Football - Brazzaville
-- Script Complet : DML + DQL
-- ============================================================

USE LigueFootball;
GO

-- ============================================================
-- PARTIE A — DML (INSERT, UPDATE, DELETE)
-- ============================================================

-- ============================================================
-- EXERCICE 1 — Insérer les 8 équipes
-- ============================================================

INSERT INTO equipes (nom_equipe, quartier, entraineur, annee_creation)
VALUES 
    ('AS Poto-Poto', 'Poto-Poto', 'Jean Malonga', 2010),
    ('FC Bacongo', 'Bacongo', 'Pierre Nzaou', 2008),
    ('Étoile de Moungali', 'Moungali', 'Serge Loubaki', 2015),
    ('Ouenzé United', 'Ouenzé', 'Alain Mabilala', 2012),
    ('Talangai FC', 'Talangai', 'Bruno Nguobai', 2011),
    ('Makélékélé Sport', 'Makélékélé', 'Rufin Massamba', 2009),
    ('AS Mfilou', 'Mfilou', 'Claude Ondongo', 2013),
    ('Djiri Football Club', 'Djiri', 'Fabrice Kimbembe', 2014);

-- ============================================================
-- EXERCICE 2 — Insérer 3 stades et des joueurs
-- ============================================================

-- a) Insérer 3 stades
INSERT INTO stades (nom_stade, quartier, capacite)
VALUES 
    ('Stade Alphonse Massemba-Débat', 'Poto-Poto', 15000),
    ('Stade Augustin Poignet', 'Bacongo', 8000),
    ('Stade de Moungali', 'Moungali', 5000);

-- b) Insérer au moins 3 joueurs par équipe

-- AS Poto-Poto (équipe 1)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Mavoungou', 'Christian', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')),
    ('Nganga', 'Jean', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')),
    ('Mboungou', 'Pierre', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')),
    ('Lekoundzou', 'Alain', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto'));

-- FC Bacongo (équipe 2)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Nzamba', 'François', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo')),
    ('Loumou', 'Robert', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo')),
    ('Mfoutou', 'Richard', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo')),
    ('Kouka', 'Marcel', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo'));

-- Étoile de Moungali (équipe 3)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Mabiala', 'Jacques', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali')),
    ('Ndinga', 'Luc', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali')),
    ('Massamba', 'David', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali')),
    ('Boukoulou', 'Paul', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali'));

-- Ouenzé United (équipe 4)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Kimbembe', 'André', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenzé United')),
    ('Ntsoumou', 'Georges', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenzé United')),
    ('Moyen', 'Claude', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenzé United')),
    ('Bayonne', 'Henri', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenzé United'));

-- Talangai FC (équipe 5)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Nguimbi', 'Firmin', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC')),
    ('Mbou', 'Alexis', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC')),
    ('Monga', 'Eugène', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC')),
    ('Ntoutoume', 'Joseph', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC'));

-- Makélékélé Sport (équipe 6)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Kibangou', 'Hervé', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport')),
    ('Mangou', 'Patrice', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport')),
    ('Mboungou', 'Thierry', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport')),
    ('Massamba', 'Jean', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport'));

-- AS Mfilou (équipe 7)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Nzaou', 'Martin', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou')),
    ('Moukala', 'Simon', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou')),
    ('Kamba', 'Daniel', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou')),
    ('Ndouba', 'Franck', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou'));

-- Djiri Football Club (équipe 8)
INSERT INTO joueurs (nom, prenom, poste, equipe_id)
VALUES 
    ('Moukagni', 'Nestor', 'Gardien', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club')),
    ('Mboungou', 'Steve', 'Defenseur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club')),
    ('Bouka', 'Pascal', 'Milieu', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club')),
    ('Mangou', 'Éric', 'Attaquant', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club'));

-- ============================================================
-- EXERCICE 3 — Insérer 6 matchs de la 1ère journée
-- ============================================================

INSERT INTO matchs (equipe_domicile_id, equipe_exterieur_id, date_match, stade_id, score_domicile, score_exterieur)
VALUES 
    -- Match 1
    ((SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto'),
     (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo'),
     '2026-08-15 15:00:00',
     (SELECT stade_id FROM stades WHERE nom_stade = 'Stade Alphonse Massemba-Débat'),
     0, 0),
    
    -- Match 2
    ((SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali'),
     (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenzé United'),
     '2026-08-15 15:00:00',
     (SELECT stade_id FROM stades WHERE nom_stade = 'Stade Augustin Poignet'),
     0, 0),
    
    -- Match 3
    ((SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC'),
     (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport'),
     '2026-08-15 15:00:00',
     (SELECT stade_id FROM stades WHERE nom_stade = 'Stade de Moungali'),
     0, 0),
    
    -- Match 4
    ((SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou'),
     (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club'),
     '2026-08-15 15:00:00',
     (SELECT stade_id FROM stades WHERE nom_stade = 'Stade Alphonse Massemba-Débat'),
     0, 0),
    
    -- Match 5
    ((SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto'),
     (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali'),
     '2026-08-15 15:00:00',
     (SELECT stade_id FROM stades WHERE nom_stade = 'Stade Augustin Poignet'),
     0, 0),
    
    -- Match 6
    ((SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo'),
     (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenzé United'),
     '2026-08-15 15:00:00',
     (SELECT stade_id FROM stades WHERE nom_stade = 'Stade de Moungali'),
     0, 0);

-- ============================================================
-- EXERCICE 4 — UPDATE — Enregistrer les résultats
-- ============================================================

-- a) Mettre à jour les scores des 6 matchs

-- Match 1: AS Poto-Poto 2 - 1 FC Bacongo
UPDATE matchs 
SET score_domicile = 2, score_exterieur = 1
WHERE match_id = 1;

-- Match 2: Étoile de Moungali 1 - 1 Ouenzé United
UPDATE matchs 
SET score_domicile = 1, score_exterieur = 1
WHERE match_id = 2;

-- Match 3: Talangai FC 3 - 0 Makélékélé Sport
UPDATE matchs 
SET score_domicile = 3, score_exterieur = 0
WHERE match_id = 3;

-- Match 4: AS Mfilou 0 - 2 Djiri Football Club
UPDATE matchs 
SET score_domicile = 0, score_exterieur = 2
WHERE match_id = 4;

-- Match 5: AS Poto-Poto 2 - 2 Étoile de Moungali
UPDATE matchs 
SET score_domicile = 2, score_exterieur = 2
WHERE match_id = 5;

-- Match 6: FC Bacongo 1 - 0 Ouenzé United
UPDATE matchs 
SET score_domicile = 1, score_exterieur = 0
WHERE match_id = 6;

-- b) Corriger le stade d'un match (Match 5 joué à Moungali)
UPDATE matchs 
SET stade_id = (SELECT stade_id FROM stades WHERE nom_stade = 'Stade de Moungali')
WHERE match_id = 5;

-- ============================================================
-- EXERCICE 5 — INSERT — Enregistrer les buteurs
-- ============================================================

-- Match 1: AS Poto-Poto 2 - 1 FC Bacongo
-- Buts AS Poto-Poto
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (1, (SELECT joueur_id FROM joueurs WHERE nom = 'Lekoundzou' AND prenom = 'Alain' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')), 23),
    (1, (SELECT joueur_id FROM joueurs WHERE nom = 'Mboungou' AND prenom = 'Pierre' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')), 67);

-- But FC Bacongo
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (1, (SELECT joueur_id FROM joueurs WHERE nom = 'Kouka' AND prenom = 'Marcel' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo')), 45);

-- Match 2: Étoile de Moungali 1 - 1 Ouenzé United
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (2, (SELECT joueur_id FROM joueurs WHERE nom = 'Boukoulou' AND prenom = 'Paul' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali')), 34),
    (2, (SELECT joueur_id FROM joueurs WHERE nom = 'Bayonne' AND prenom = 'Henri' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenzé United')), 78);

-- Match 3: Talangai FC 3 - 0 Makélékélé Sport
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (3, (SELECT joueur_id FROM joueurs WHERE nom = 'Ntoutoume' AND prenom = 'Joseph' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC')), 12),
    (3, (SELECT joueur_id FROM joueurs WHERE nom = 'Ntoutoume' AND prenom = 'Joseph' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC')), 55),
    (3, (SELECT joueur_id FROM joueurs WHERE nom = 'Monga' AND prenom = 'Eugène' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangai FC')), 89);

-- Match 4: AS Mfilou 0 - 2 Djiri Football Club
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (4, (SELECT joueur_id FROM joueurs WHERE nom = 'Mangou' AND prenom = 'Éric' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club')), 28),
    (4, (SELECT joueur_id FROM joueurs WHERE nom = 'Bouka' AND prenom = 'Pascal' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club')), 74);

-- Match 5: AS Poto-Poto 2 - 2 Étoile de Moungali
-- Buts AS Poto-Poto
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (5, (SELECT joueur_id FROM joueurs WHERE nom = 'Lekoundzou' AND prenom = 'Alain' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')), 15),
    (5, (SELECT joueur_id FROM joueurs WHERE nom = 'Mboungou' AND prenom = 'Pierre' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')), 72);

-- Buts Étoile de Moungali
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (5, (SELECT joueur_id FROM joueurs WHERE nom = 'Massamba' AND prenom = 'David' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali')), 44),
    (5, (SELECT joueur_id FROM joueurs WHERE nom = 'Boukoulou' AND prenom = 'Paul' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Étoile de Moungali')), 90);

-- Match 6: FC Bacongo 1 - 0 Ouenzé United
INSERT INTO buts (match_id, joueur_id, minute)
VALUES 
    (6, (SELECT joueur_id FROM joueurs WHERE nom = 'Mfoutou' AND prenom = 'Richard' AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo')), 63);

-- ============================================================
-- EXERCICE 6 — DELETE — Corriger une erreur de saisie
-- ============================================================

-- Vérifier d'abord combien de lignes correspondent au joueur en double
SELECT COUNT(*) AS nombre_doublons, joueur_id, nom, prenom, equipe_id
FROM joueurs
WHERE nom = 'Mboungou' AND prenom = 'Pierre'
GROUP BY joueur_id, nom, prenom, equipe_id;

-- Supprimer le doublon (garder l'ID le plus petit)
DELETE FROM joueurs 
WHERE joueur_id = (
    SELECT MAX(joueur_id) 
    FROM joueurs 
    WHERE nom = 'Mboungou' 
      AND prenom = 'Pierre'
      AND equipe_id = (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto')
);

-- ============================================================
-- PARTIE B — DQL (SELECT)
-- ============================================================

-- ============================================================
-- EXERCICE 7 — Explorer les données
-- ============================================================

-- a) Nombre d'équipes enregistrées
SELECT COUNT(*) AS nombre_equipes FROM equipes;

-- b1) Nombre total de joueurs
SELECT COUNT(*) AS total_joueurs FROM joueurs;

-- b2) Nombre de joueurs par équipe
SELECT 
    e.nom_equipe,
    COUNT(j.joueur_id) AS nombre_joueurs
FROM equipes e
LEFT JOIN joueurs j ON e.equipe_id = j.equipe_id
GROUP BY e.nom_equipe
ORDER BY nombre_joueurs DESC;

-- c) Nombre total de buts marqués sur la journée
SELECT COUNT(*) AS total_buts FROM buts;

-- (Bonus) Détail des buts par match
SELECT 
    m.match_id,
    e_domicile.nom_equipe AS equipe_domicile,
    e_exterieur.nom_equipe AS equipe_exterieur,
    m.score_domicile,
    m.score_exterieur,
    COUNT(b.but_id) AS buts_marques
FROM matchs m
JOIN equipes e_domicile ON m.equipe_domicile_id = e_domicile.equipe_id
JOIN equipes e_exterieur ON m.equipe_exterieur_id = e_exterieur.equipe_id
LEFT JOIN buts b ON m.match_id = b.match_id
GROUP BY m.match_id, e_domicile.nom_equipe, e_exterieur.nom_equipe, m.score_domicile, m.score_exterieur
ORDER BY m.match_id;

-- ============================================================
-- EXERCICE 8 — Filtrage, tri et agrégation
-- ============================================================

-- a) Liste de tous les joueurs qui jouent au poste "Attaquant"
SELECT 
    j.nom,
    j.prenom,
    j.equipe_id,
    e.nom_equipe
FROM joueurs j
JOIN equipes e ON j.equipe_id = e.equipe_id
WHERE j.poste = 'Attaquant'
ORDER BY e.nom_equipe, j.nom;

-- b) Liste des matchs où plus de 3 buts ont été marqués au total
SELECT 
    m.match_id,
    e_domicile.nom_equipe AS equipe_domicile,
    e_exterieur.nom_equipe AS equipe_exterieur,
    m.score_domicile,
    m.score_exterieur,
    (m.score_domicile + m.score_exterieur) AS total_buts
FROM matchs m
JOIN equipes e_domicile ON m.equipe_domicile_id = e_domicile.equipe_id
JOIN equipes e_exterieur ON m.equipe_exterieur_id = e_exterieur.equipe_id
WHERE (m.score_domicile + m.score_exterieur) > 3
ORDER BY total_buts DESC;

-- c) Nombre de joueurs par équipe (trié du plus grand au plus petit)
SELECT 
    e.equipe_id,
    e.nom_equipe,
    COUNT(j.joueur_id) AS nombre_joueurs
FROM equipes e
LEFT JOIN joueurs j ON e.equipe_id = j.equipe_id
GROUP BY e.equipe_id, e.nom_equipe
ORDER BY nombre_joueurs DESC;

-- d) Score total de chaque match (trié du plus spectaculaire au moins spectaculaire)
SELECT 
    m.match_id,
    e_domicile.nom_equipe AS equipe_domicile,
    e_exterieur.nom_equipe AS equipe_exterieur,
    m.score_domicile,
    m.score_exterieur,
    (m.score_domicile + m.score_exterieur) AS score_total
FROM matchs m
JOIN equipes e_domicile ON m.equipe_domicile_id = e_domicile.equipe_id
JOIN equipes e_exterieur ON m.equipe_exterieur_id = e_exterieur.equipe_id
ORDER BY score_total DESC, m.match_id;

-- ============================================================
-- REQUÊTES DE VÉRIFICATION SUPPLÉMENTAIRES
-- ============================================================

-- Vue d'ensemble du championnat
SELECT 
    'Équipes' AS categorie,
    COUNT(*) AS nombre
FROM equipes
UNION ALL
SELECT 
    'Joueurs' AS categorie,
    COUNT(*) AS nombre
FROM joueurs
UNION ALL
SELECT 
    'Matchs' AS categorie,
    COUNT(*) AS nombre
FROM matchs
UNION ALL
SELECT 
    'Buts' AS categorie,
    COUNT(*) AS nombre
FROM buts;

-- Classement des buteurs (seulement ceux qui ont marqué)
SELECT 
    j.nom,
    j.prenom,
    e.nom_equipe,
    COUNT(b.but_id) AS buts_marques
FROM joueurs j
JOIN equipes e ON j.equipe_id = e.equipe_id
LEFT JOIN buts b ON j.joueur_id = b.joueur_id
GROUP BY j.nom, j.prenom, e.nom_equipe
HAVING COUNT(b.but_id) > 0
ORDER BY buts_marques DESC, j.nom;

-- Détail complet des matchs avec tous les buteurs
SELECT 
    m.match_id,
    e_domicile.nom_equipe AS equipe_domicile,
    e_exterieur.nom_equipe AS equipe_exterieur,
    m.score_domicile,
    m.score_exterieur,
    s.nom_stade,
    STRING_AGG(CONCAT(j.prenom, ' ', j.nom, ' (', b.minute, ')'), ', ') AS buteurs
FROM matchs m
JOIN equipes e_domicile ON m.equipe_domicile_id = e_domicile.equipe_id
JOIN equipes e_exterieur ON m.equipe_exterieur_id = e_exterieur.equipe_id
JOIN stades s ON m.stade_id = s.stade_id
LEFT JOIN buts b ON m.match_id = b.match_id
LEFT JOIN joueurs j ON b.joueur_id = j.joueur_id
GROUP BY m.match_id, e_domicile.nom_equipe, e_exterieur.nom_equipe, 
         m.score_domicile, m.score_exterieur, s.nom_stade
ORDER BY m.match_id;