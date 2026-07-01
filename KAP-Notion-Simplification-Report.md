# KAP Notion Simplification & Access Report

## 1. État Actuel des Accès Notion

J'ai testé les deux tokens en notre possession :

*   **TOKEN A (`ntn_144641...`) : MANUS Y-world**
    *   **Statut :** ACTIF ET PUISSANT
    *   **Accès :** 100+ bases de données accessibles.
    *   **Problème :** Il n'a pas accès à la base `Manus Memory — Sessions` (`5e51ded4`).
*   **TOKEN B (`ntn_3949...`) : YOS Comet-Light (legacy)**
    *   **Statut :** OBSOLÈTE
    *   **Accès :** 0 base de données accessible.

## 2. Plan de Simplification Radicale ("FULL ACCESS")

Tu as raison, la gestion actuelle des intégrations Notion est confuse (Manus, Manus 2, Comet-Light...). Voici comment obtenir un **FULL ACCESS** définitif et simple :

### Étape 1 : Nettoyage (dans Notion)
1.  Va dans Notion > Settings & members > My connections.
2.  **Supprime** toutes les anciennes intégrations : "YOS Comet-Light", "Manus 2", etc.
3.  Ne garde **QUE** l'intégration officielle nommée **"MANUS"** (celle associée au Token A).

### Étape 2 : Le FULL ACCESS définitif
Au lieu de partager page par page (ce qui cause nos blocages actuels), tu peux donner accès à tout l'espace de travail d'un coup :

1.  Dans Notion, va dans **Settings & members** > **Connections**.
2.  Trouve l'intégration **MANUS**.
3.  Clique sur les trois petits points `...` à côté.
4.  Assure-toi que l'accès est défini sur **All workspaces pages** (Toutes les pages de l'espace de travail) et non sur "Selected pages only".
5.  Si cette option n'est pas disponible, va à la racine de ton espace de travail (le dossier parent le plus haut) et partage-le avec l'intégration MANUS. L'accès se propagera en cascade à toutes les sous-pages et bases de données, y compris les Sessions.

## 3. Résultats de l'Extraction WP2-M2B (en parallèle)

Pendant que nous réglions Notion, j'ai exécuté le script WP2-M2B demandé par ChatGPT :

*   **Manus API :** Découverte majeure ! L'API ne contient pas 2392 tâches, mais **plus de 10 000 tâches**. J'ai extrait les métadonnées des 10 000 tâches.
*   **Mem0 :** Extraction complète réussie (316 mémoires).
*   **Knowledge API :** L'API Manus ne permet pas l'extraction directe du contenu Knowledge (erreur 404 sur ces endpoints).
*   **Sessions DB :** Toujours en attente du FULL ACCESS Notion pour l'extraire.

Le fichier ZIP `KAP-WP2-M2B-Full-Manus-API-Harvest.zip` contenant les 32 rapports demandés par ChatGPT est prêt.
