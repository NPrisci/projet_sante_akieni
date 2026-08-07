/* =========================================================
   PROJET FIL ROUGE SQL
   Ligue Communale de Football — Brazzaville
   Semaine 9 — SQL Fondamentaux 1
   ========================================================= */


/* =========================================================
   EXERCICE 1 — CRÉATION DE LA BASE
   ========================================================= */

-- Indice : CREATE DATABASE LigueFootball; 
CREATE DATABASE LigueFootball;
GO


--  Commencez par USE LigueFootball; 
USE LigueFootball;
GO


/* =========================================================
   EXERCICE 2 — TABLES RACINES
   ========================================================= */

-- Consigne : 2 instructions CREATE TABLE.
CREATE TABLE equipes (
    equipe_id INT PRIMARY KEY IDENTITY(1,1),
    nom_equipe VARCHAR(50) NOT NULL,
    quartier VARCHAR(50) NOT NULL,
    entraineur VARCHAR(50),
    annee_creation INT
);
GO

CREATE TABLE stades (
    stade_id INT PRIMARY KEY IDENTITY(1,1),
    nom_stade VARCHAR(50) NOT NULL,
    quartier VARCHAR(50),
    capacite INT
);
GO


/* =========================================================
   EXERCICE 3 — TABLE JOUEURS
   ========================================================= */

CREATE TABLE joueurs (
    joueur_id INT PRIMARY KEY IDENTITY(1,1),
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    equipe_id INT,
    poste VARCHAR(20) NOT NULL,
    numero_maillot INT,
    date_naissance DATE,

    CONSTRAINT FK_joueurs_equipes
        FOREIGN KEY (equipe_id)
        REFERENCES equipes(equipe_id)
);
GO


/* =========================================================
   EXERCICE 3 — TABLE MATCHS
   ========================================================= */

CREATE TABLE matchs (
    match_id INT PRIMARY KEY IDENTITY(1,1),
    equipe_domicile_id INT,
    equipe_exterieur_id INT,
    stade_id INT,
    date_match DATE NOT NULL,
    score_domicile INT DEFAULT 0,
    score_exterieur INT DEFAULT 0,

    CONSTRAINT FK_matchs_equipe_domicile
        FOREIGN KEY (equipe_domicile_id)
        REFERENCES equipes(equipe_id),

    CONSTRAINT FK_matchs_equipe_exterieur
        FOREIGN KEY (equipe_exterieur_id)
        REFERENCES equipes(equipe_id),

    CONSTRAINT FK_matchs_stade
        FOREIGN KEY (stade_id)
        REFERENCES stades(stade_id)
);
GO


/* =========================================================
   EXERCICE 3 — TABLE BUTS
   ========================================================= */

CREATE TABLE buts (
    but_id INT PRIMARY KEY IDENTITY(1,1),
    match_id INT,
    joueur_id INT,
    minute INT,

    CONSTRAINT FK_buts_matchs
        FOREIGN KEY (match_id)
        REFERENCES matchs(match_id),

    CONSTRAINT FK_buts_joueurs
        FOREIGN KEY (joueur_id)
        REFERENCES joueurs(joueur_id)
);
GO


/* =========================================================
   EXERCICE 4 — CONTRAINTE CHECK
   ========================================================= */

ALTER TABLE joueurs
ADD CONSTRAINT CK_joueurs_poste
CHECK (poste IN (
    'Gardien',
    'Défenseur',
    'Milieu',
    'Attaquant'
));
GO


/* =========================================================
   EXERCICE 5 — COLONNE CALCULÉE
   ========================================================= */

ALTER TABLE matchs
ADD diff_buts AS (
    score_domicile - score_exterieur
);
GO


/* =========================================================
   EXERCICE 6 — AJOUT DE COLONNES
   ========================================================= */

ALTER TABLE joueurs
ADD
    capitaine BIT NOT NULL
        CONSTRAINT DF_joueurs_capitaine DEFAULT 0,
    telephone VARCHAR(20);
GO


/* =========================================================
   EXERCICE 7 — TABLE TEMPORAIRE DE TEST
   ========================================================= */

-- a) Créez une table temporaire test_saison avec 3 colonnes de votre choix. 
CREATE TABLE test_saison (
    id INT,
    nom VARCHAR(50),
    annee INT
);
GO

-- b) Renommez-la en test_saison_v2 avec sp_rename. 
EXEC sp_rename
    'test_saison',
    'test_saison_v2';
GO

-- c) Supprimez-la avec DROP TABLE. 
DROP TABLE test_saison_v2;
GO


/* =========================================================
   EXERCICE 8-a — INDEX
   ========================================================= */

CREATE NONCLUSTERED INDEX IX_matchs_date_match
ON matchs(date_match);
GO


/* =========================================================
   EXERCICE 8-b — VÉRIFICATION DU SCHÉMA
   ========================================================= */

SELECT
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_CATALOG = 'LigueFootball'
ORDER BY
    TABLE_NAME,
    ORDINAL_POSITION;
GO