# Plan de Fusion Complet v2 - Session Navigator Skill

## Métadonnées

**Date** : 2026-02-15  
**Sessions sources** :
- Session A : https://manus.im/share/sVUnGFiX7EYxQB47zcdsEA (Data Layer)
- Session B : https://manus.im/share/iDnRc9aX7GXxhoPKUQdsEY (UI Layer)

**Objectif** : Créer le skill `session-navigator` avec workflow complet CLOSE/ARCHIVE/FUSION

---

## 1. Architecture Complète du Skill

### 1.1 Qu'est-ce que le Skill ?

**Nom** : `session-navigator`  
**Type** : Skill Manus  
**Fonction** : Gérer le cycle de vie complet des sessions Manus

**Capacités** :
1. **Visualiser** : Tree view hiérarchique des sessions
2. **Organiser** : Tags, projets, hiérarchies
3. **Fusionner** : Combiner sessions similaires en MASTER SESSIONS
4. **Archiver** : Sauvegarder dans Notion avec synthèse
5. **Clore** : Marquer sessions terminées
6. **Rechercher** : Vector DB + full-text search

### 1.2 Workflow CLOSE / ARCHIVE / FUSION

```
┌─────────────────────────────────────────────────────────┐
│                   SESSION LIFECYCLE                      │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ ACTIVE SESSION│
                  │  (MAJUSCULE)  │
                  └───────┬───────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    ┌─────────┐     ┌─────────┐    ┌──────────┐
    │  CLOSE  │     │ ARCHIVE │    │  FUSION  │
    │(minusc) │     │ (Notion)│    │ (MASTER) │
    └─────────┘     └─────────┘    └──────────┘
          │               │               │
          └───────────────┴───────────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   ARCHIVED    │
                  │  (read-only)  │
                  └───────────────┘
```

#### CLOSE (END)
**Action** : Fermer une session  
**Effet** :
- Titre → minuscule
- Ajout `(closed YYYY-MM-DD)` au titre
- Synthèse finale ajoutée en fin de session
- Session devient read-only (suggestion)

**Synthèse finale contient** :
- Résumé 2-3 lignes
- Livrables clés
- Open items
- Metrics (durée, messages, fichiers)

#### ARCHIVE
**Action** : CLOSE + Sauvegarder dans Notion  
**Effet** :
- Tout ce que fait CLOSE
- Export verbatim vers Notion Memory Hub
- Création d'une page Notion avec :
  - Titre original
  - Type : 📝 Conversation Archive
  - Tags extraits
  - Synthèse structurée
  - Action items
  - Liens vers fichiers créés
- Embedding dans vector DB pour recherche sémantique

#### FUSION
**Action** : CLOSE + Combiner dans MASTER SESSION  
**Effet** :
- Sessions sources → CLOSE
- Création nouvelle session MAJUSCULE
- Synthèse intelligente sans perte d'info
- ToC + liens vers sessions sources
- Metadata fusion en header
- Option : ARCHIVE la master session aussi

**FUSION + ARCHIVE** :
- Fusion d'abord
- Puis archive de la master session
- Sessions sources archivées séparément avec ref vers master

### 1.3 Modes de Fusion

#### Manuel (via Tree View)
1. User sélectionne sessions dans tree
2. Ordre de fusion défini manuellement
3. Clic "Merge Selected"
4. Preview de la fusion
5. Validation user
6. Exécution

#### Semi-Auto
**Trigger** : Commande `"Regroup sessions about Project A"`  
**Process** :
1. Recherche sémantique (vector DB) des sessions liées à Project A
2. Scoring de similarité
3. Proposition de groupes à fusionner
4. User valide chaque groupe
5. Exécution batch

#### Full Auto (Scheduled)
**Trigger** : Cron 1x/semaine  
**Process** :
1. Analyse toutes sessions non-fusionnées/non-archivées
2. Détection de clusters similaires (vector DB + heuristiques)
3. Proposition de fusions dans MASTER SESSIONS existantes ou nouvelles
4. Notification user avec preview
5. User valide ou rejette
6. Exécution

**Heuristiques** :
- Même projet mentionné
- Tags communs (>50%)
- Timestamps proches (<7 jours)
- Similarité sémantique (>0.75)

---

## 2. Composants du Skill

### 2.1 Structure Fichiers

```
/home/ubuntu/skills/session-navigator/
├── SKILL.md                          # Doc principale
├── README.md                         # Guide utilisateur
├── .git/                             # Git repo pour backup
├── data/
│   ├── scripts/
│   │   ├── generate_sessions_tree_v2.py
│   │   ├── generate_sessions_tree_v3_enriched.py
│   │   └── close_session.py          # NEW
│   ├── examples/
│   │   ├── yos_sessions_tree_only.json
│   │   └── yos_sessions_enriched_v2.json
│   └── backups/                      # NEW - Git-tracked backups
│       └── sessions/
│           ├── YYYY-MM-DD_HH-MM-SS_session_id.json
│           └── ...
├── fusion/
│   ├── fusion_engine.py              # NEW - Core fusion logic
│   ├── vector_search.py              # NEW - Vector DB integration
│   ├── templates/
│   │   ├── master_session_template.md
│   │   └── archive_cartouche_template.md
│   └── validators/
│       ├── info_loss_validator.py    # NEW
│       └── readability_validator.py  # NEW
├── ui/
│   ├── client/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── TreeNode.tsx
│   │   │   │   ├── SelectionPanel.tsx
│   │   │   │   ├── FilterSidebar.tsx
│   │   │   │   ├── FusionDialog.tsx  # NEW
│   │   │   │   └── ArchiveDialog.tsx # NEW
│   │   │   ├── contexts/
│   │   │   │   └── TreeContext.tsx
│   │   │   ├── api/
│   │   │   │   └── api_client.ts
│   │   │   └── types/
│   │   │       └── session.ts
│   │   └── package.json
│   └── server/
│       ├── tree_view_server.py
│       └── routes/
│           ├── fusion.py             # NEW
│           ├── archive.py            # NEW
│           └── close.py              # NEW
├── integrations/
│   ├── notion_archiver.py            # NEW
│   ├── vector_db_client.py           # NEW - Embedding + search
│   └── git_backup.py                 # NEW
├── docs/
│   ├── architecture.md
│   ├── workflows.md                  # NEW - CLOSE/ARCHIVE/FUSION
│   ├── test_results.md
│   ├── yos_terminology.md
│   └── api_reference.md
└── tests/
    ├── integration_tests.md
    └── fusion_tests.py               # NEW
```

### 2.2 Nouveaux Composants

#### `fusion_engine.py`
**Rôle** : Logique de fusion intelligente

**Fonctions** :
- `analyze_sessions(session_ids)` → Similarity matrix
- `merge_sessions(session_ids, strategy)` → Master session content
- `validate_merge(master, sources)` → Info loss score
- `create_master_session(content, metadata)` → New session

**Stratégies** :
- `chronological` : Ordre temporel
- `thematic` : Groupement par thème
- `hierarchical` : Parent → children
- `synthesis` : LLM-powered intelligent merge

#### `vector_search.py`
**Rôle** : Recherche sémantique via vector DB

**Fonctions** :
- `embed_session(session_id)` → Vector
- `search_similar(query, top_k)` → Similar sessions
- `cluster_sessions(session_ids)` → Groups
- `suggest_merges()` → Merge proposals

**Vector DB** : Chroma (local) ou Pinecone (cloud)

#### `git_backup.py`
**Rôle** : Backup automatique + rollback

**Fonctions** :
- `backup_session(session_id)` → JSON export + Git commit
- `rollback_session(session_id, commit_hash)` → Restore
- `list_backups(session_id)` → History
- `auto_backup_on_change()` → Hook

**Git Workflow** :
```bash
# Chaque modification de session = commit
git add data/backups/sessions/2026-02-15_18-00-00_session_abc.json
git commit -m "Backup session_abc before fusion"
git push origin main

# Rollback si fusion échoue
git revert <commit_hash>
```

#### `notion_archiver.py`
**Rôle** : Export vers Notion Memory Hub

**Fonctions** :
- `archive_session(session_id)` → Notion page
- `extract_metadata(session)` → Tags, status, priority
- `create_synthesis(session)` → Structured summary
- `link_to_master(session_id, master_id)` → Cross-reference

---

## 3. Plan de Fusion Exécutable

### Phase 0 : Backup Automatique

**Actions** :
1. Init Git repo dans `/home/ubuntu/skills/session-navigator/`
2. Export Session A → JSON
3. Export Session B → JSON
4. Git commit : `"Backup sessions before fusion"`
5. Push to remote (GitHub)

**Validation** :
- [ ] Git repo créé
- [ ] 2 JSON backups présents
- [ ] Commit hash sauvegardé

### Phase 1 : Analyse Technique

**Actions** :
1. Charger contenus Session A + B
2. Calculer metrics :
   - Chars total : A + B
   - Concepts uniques : Liste exhaustive
   - Overlaps : % de contenu dupliqué
   - Liens internes : Count
3. Générer rapport d'analyse

**Validation** :
- [ ] Metrics calculées
- [ ] Rapport généré
- [ ] Info loss estimé <5%

### Phase 2 : Fusion Intelligente

**Actions** :
1. Créer structure master session :
   ```markdown
   ---
   TYPE: MASTER SESSION (FUSION)
   SOURCES: 
     - Session A: [link] (Data Layer - 2026-02-15)
     - Session B: [link] (UI Layer - 2026-02-15)
   FUSION_DATE: 2026-02-15
   FUSION_METHOD: Hybrid (Synthesis + Restructuration)
   TAGS: yOS, session-navigator, tree-view, notion, manus
   STATUS: ACTIVE
   ---
   
   # YOS SESSION NAVIGATOR - MASTER SESSION
   
   > **Note** : Cette session est la fusion de [Session A](#) et [Session B](#).
   > Voir [ToC](#toc) pour navigation rapide.
   
   ## Synthèse des Sessions Sources
   
   ### Session A - Data Layer
   [Résumé 3-4 lignes]
   
   ### Session B - UI Layer
   [Résumé 3-4 lignes]
   
   ---
   
   ## Table des Matières {#toc}
   
   1. [Architecture Globale](#architecture)
   2. [Data Layer](#data-layer)
      - [Scripts Python](#scripts)
      - [JSON Generation](#json)
   3. [UI Layer](#ui-layer)
      - [React Components](#components)
      - [API Server](#api)
   4. [Intégration](#integration)
   5. [Tests](#tests)
   6. [Open Items](#open-items)
   7. [Annexes](#annexes)
   
   ---
   
   ## 1. Architecture Globale {#architecture}
   
   [Synthèse combinée des 2 sessions]
   
   > **Source** : Concept développé dans [Session A - Phase 2](#session-a-phase-2)
   
   ...
   ```

2. Synthétiser contenu :
   - Supprimer redondances
   - Fusionner concepts similaires
   - Restructurer pour lisibilité
   - Ajouter liens internes
   - Préserver TOUT le sens

3. Valider lisibilité :
   - Flesch Reading Ease >60
   - Headings max 4 niveaux
   - ToC max 3 niveaux
   - Paragraphes <5 lignes

**Validation** :
- [ ] Master session créée
- [ ] ToC complet
- [ ] Liens vers sources fonctionnels
- [ ] Lisibilité validée

### Phase 3 : Validation Technique

**Actions** :
1. Calculer info loss score :
   ```python
   concepts_A = extract_concepts(session_A)
   concepts_B = extract_concepts(session_B)
   concepts_master = extract_concepts(master_session)
   
   loss_score = 1 - (len(concepts_master) / (len(concepts_A) + len(concepts_B)))
   # Target: loss_score < 0.05 (5%)
   ```

2. Vérifier liens cassés
3. Tester tous les scripts/code mentionnés
4. Générer diff report

**Validation** :
- [ ] Info loss <5%
- [ ] Aucun lien cassé
- [ ] Code testé
- [ ] Diff report approuvé

### Phase 4 : Validation Manuelle (User)

**Actions** :
1. Présenter master session à user
2. User lit intégralement (dry read)
3. User valide :
   - Clarté
   - Complétude
   - Pertinence
4. User approuve ou demande ajustements

**Validation** :
- [ ] User a lu
- [ ] User approuve
- [ ] Ajustements appliqués (si demandés)

### Phase 5 : Archive Sessions Sources

**Actions** :
1. CLOSE Session A :
   - Titre → minuscule
   - Ajout `(closed 2026-02-15)`
   - Synthèse finale
2. CLOSE Session B (idem)
3. ARCHIVE Session A → Notion
4. ARCHIVE Session B → Notion
5. Ajouter refs vers master session dans archives

**Template Archive** :
```markdown
---
SESSION ARCHIVÉE - 2026-02-15

**Raison** : Fusionnée dans [YOS SESSION NAVIGATOR - MASTER](#master-link)

**Synthèse** :
Cette session a développé la couche data (scripts Python, JSON generation, 
tests d'intégration) pour le yOS Session Navigator.

**Livrables clés** :
- `generate_sessions_tree_v2.py`
- `generate_sessions_tree_v3_enriched.py`
- `yos_sessions_tree_only.json` (validé)
- Documentation complète

**Open Items** : Transférés vers [Master Session - Open Items](#master-open-items)

**Metrics** :
- Durée : 3h
- Messages : 42
- Fichiers créés : 7
- Chars : 125,000

**Note** : Contenu intégral préservé dans master session.
---
```

**Validation** :
- [ ] Sessions A+B closed
- [ ] Archives Notion créées
- [ ] Refs vers master ajoutées

### Phase 6 : Création du Skill Physique

**Actions** :
1. Créer structure `/home/ubuntu/skills/session-navigator/`
2. Copier tous fichiers Session A → `data/`
3. Copier tous fichiers Session B → `ui/`
4. Créer nouveaux composants (fusion_engine, vector_search, etc.)
5. Créer SKILL.md complet
6. Git commit : `"Initial skill creation from fusion"`

**Validation** :
- [ ] Structure complète
- [ ] Tous fichiers présents
- [ ] SKILL.md complet
- [ ] Git commit effectué

### Phase 7 : Tests End-to-End

**Actions** :
1. Tester data layer :
   - Génération JSON
   - Upload dans tree view
2. Tester UI layer :
   - Tree view rendering
   - Selection
   - Batch operations
3. Tester fusion workflow :
   - Manuel
   - Semi-auto
   - Full auto (simulation)
4. Tester backup/rollback

**Validation** :
- [ ] Data layer OK
- [ ] UI layer OK
- [ ] Fusion workflow OK
- [ ] Backup/rollback OK

### Phase 8 : Intégration Vector DB

**Actions** :
1. Setup Chroma local
2. Embed toutes sessions archivées
3. Tester recherche sémantique
4. Tester clustering
5. Tester suggestions de fusion

**Validation** :
- [ ] Vector DB opérationnel
- [ ] Embeddings créés
- [ ] Recherche fonctionnelle
- [ ] Suggestions pertinentes

---

## 4. Système de Backup & Rollback

### 4.1 Git comme Solution Générale

**Principe** : Chaque session = Git repo

**Structure** :
```
/home/ubuntu/.manus_sessions_backup/
├── .git/
├── sessions/
│   ├── session_abc123/
│   │   ├── metadata.json
│   │   ├── content.md
│   │   ├── files/
│   │   └── history/
│   │       ├── 2026-02-15_18-00-00.json
│   │       └── 2026-02-15_19-30-00.json
│   └── session_def456/
│       └── ...
└── README.md
```

**Workflow** :
1. **Auto-backup** : Chaque modification → Git commit
2. **Snapshot** : Avant fusion/archive → Tag Git
3. **Rollback** : `git revert <tag>` ou `git checkout <commit>`
4. **Remote backup** : Push to GitHub (private repo)

**Avantages** :
- Historique complet
- Diff natif
- Rollback simple
- Collaboration possible
- Backup remote gratuit

### 4.2 Backup Temporaire

**Durée** : 30 jours  
**Localisation** : `/home/ubuntu/.manus_sessions_backup/temp/`  
**Purge** : Cron daily, supprime >30 jours

**Après validation fusion** :
- Backups temp → Git permanent
- Tag Git : `fusion_YYYY-MM-DD_session_A_B`

### 4.3 Rollback Procedure

**Si fusion échoue** :
```bash
cd /home/ubuntu/.manus_sessions_backup/
git log --oneline | grep "fusion"
# Identifier commit avant fusion
git revert <commit_hash>
# Restaurer sessions A+B
./restore_sessions.sh session_abc session_def
```

**Validation rollback** :
- [ ] Sessions A+B restaurées
- [ ] Master session supprimée
- [ ] Notion archives supprimées
- [ ] User notifié

---

## 5. Intégration Vector DB

### 5.1 Pourquoi Vector DB ?

**Usages** :
1. **Recherche sémantique** : "Trouve sessions sur architecture yOS"
2. **Clustering** : Grouper sessions similaires automatiquement
3. **Suggestions** : "Ces 3 sessions devraient être fusionnées"
4. **Context retrieval** : Charger contexte pertinent dans nouvelles sessions

### 5.2 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Vector DB Integration                   │
└─────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    ┌─────────┐     ┌─────────┐    ┌──────────┐
    │ Chroma  │     │ Pinecone│    │  Notion  │
    │ (local) │     │ (cloud) │    │ (backup) │
    └─────────┘     └─────────┘    └──────────┘
          │               │               │
          └───────────────┴───────────────┘
                          │
                    ┌─────▼─────┐
                    │ Embeddings│
                    │  (OpenAI) │
                    └───────────┘
```

**Choix** : Chroma (local) pour MVP, Pinecone si scale

### 5.3 Workflow Embedding

**Quand embedder** :
1. Session archivée → Embed automatiquement
2. Session fusionnée → Embed master
3. Batch : 1x/jour, embed nouvelles sessions

**Contenu à embedder** :
- Titre
- Synthèse
- Tags
- Key concepts
- Open items

**Metadata** :
- session_id
- timestamp
- type (active/closed/archived/master)
- project
- tags

### 5.4 Recherche Sémantique

**Query** : `"Sessions about yOS tree view"`

**Process** :
1. Embed query → Vector
2. Search Chroma → Top 10 similar
3. Filter by metadata (type, date, project)
4. Rank by relevance
5. Return results

**UI** :
- Search bar dans tree view
- Filtres : type, date, project, tags
- Results : Cards avec preview + similarity score

### 5.5 Auto-Clustering

**Trigger** : Cron 1x/semaine

**Process** :
1. Fetch all non-archived sessions
2. Embed all
3. Clustering (K-means ou HDBSCAN)
4. Identify clusters >2 sessions
5. Propose fusions
6. User validates

**Notification** :
```
🔔 Fusion Suggestions

Cluster 1: "yOS Architecture" (3 sessions)
- Session X: Y-OS cognitive system design
- Session Y: yOS memory architecture
- Session Z: yOS agent coordination

Similarity: 0.82
Recommendation: MERGE into MASTER SESSION

[View Details] [Merge Now] [Dismiss]
```

---

## 6. Validation Finale & Checklist

### Pre-Fusion
- [x] Sessions analysées
- [x] Overlaps identifiés (0% code, 30-50% concepts)
- [x] Architecture définie
- [x] Structure cible validée
- [x] Git repo initialisé
- [x] Backups créés
- [ ] **User approval final** ⚠️

### Post-Fusion
- [ ] Master session créée
- [ ] ToC complet
- [ ] Liens fonctionnels
- [ ] Info loss <5%
- [ ] Lisibilité validée
- [ ] User a validé manuellement
- [ ] Sessions sources closed
- [ ] Archives Notion créées
- [ ] Skill physique créé
- [ ] Tests end-to-end OK
- [ ] Vector DB intégré
- [ ] Git commit final
- [ ] Documentation complète

---

## 7. Metrics de Succès

| Metric | Target | Actuel | Status |
|--------|--------|--------|--------|
| Info loss | <5% | TBD | ⏳ |
| Lisibilité (Flesch) | >60 | TBD | ⏳ |
| Liens cassés | 0 | TBD | ⏳ |
| User satisfaction | >8/10 | TBD | ⏳ |
| Temps fusion | <2h | TBD | ⏳ |
| Rollback success | 100% | TBD | ⏳ |

---

## 8. Next Steps Immédiats

1. **User approval** : Valider ce plan v2 complet
2. **Init Git repo** : Créer backup infrastructure
3. **Export sessions** : JSON backups A+B
4. **Execute Phase 1** : Analyse technique
5. **Execute Phase 2** : Fusion intelligente
6. **Iterate** : Validation → Ajustements → Re-validation

---

**Plan créé par** : Manus  
**Date** : 2026-02-15 19:15 UTC  
**Version** : 2.0 (Complete)  
**Status** : ✅ Ready for execution
