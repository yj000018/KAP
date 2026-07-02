# KAP Archive Pipeline — Runbook Technique & Procédural

**Version:** 1.0 — 2026-07-02
**Auteur:** Manus (documenté après 2 cycles d'apprentissage)
**Statut:** CANON — ne pas réinventer

---

## 1. Ce que fait le pipeline

Pour chaque session Manus non archivée :
1. Récupère le contenu (messages) via l'API Manus
2. Génère une fiche MD structurée via LLM (Claude via proxy sandbox)
3. Commit la fiche dans `/KAP/03_Archived_Sessions/YOS/{uid}_session_card.md`
4. Push sur GitHub
5. Ajoute `[✓] ` au début du titre dans Manus (marqueur visuel d'archivage)

---

## ⚠️ RÈGLE CRITIQUE — My Browser Mac uniquement

> **My Browser DOIT être utilisé depuis ton Mac (bureau ou laptop), jamais depuis iOS.**
>
> Raison : My Browser dans le sandbox Manus (machine virtuelle) ne maintient pas la session authentifiée — la page Manus se charge en mode non-connecté à chaque navigation. Seul ton navigateur Mac (Chrome/Safari) avec ta session Manus active permet de scroller la sidebar et récupérer tous les UIDs.
>
> **Processus correct :**
> 1. Sur ton **Mac** → ouvre Manus dans Chrome
> 2. Va dans Settings → Apps → My Browser → **Connect**
> 3. Reviens dans cette session Manus et dis « My Browser connecté »
> 4. Je prends le relais : je scrape la sidebar, collecte tous les UIDs, lance le pipeline

---

## 2. Ce qui fonctionne — ce qui ne fonctionne pas

### ✅ Ce qui fonctionne

| Méthode | Usage | Notes |
|---|---|---|
| **API `task.listMessages`** | Récupérer le contenu d'une session par UID | Fonctionne bien, paramètre = `task_id` |
| **API `task.update`** | Modifier le titre d'une session | Fonctionne — payload `{"task_id": uid, "title": "nouveau titre"}` |
| **API `task.list`** | Lister les sessions récentes | Limité à 200 tâches max, ne remonte pas avant ~juin 2026 |
| **LLM proxy sandbox** | Générer les fiches MD | Utiliser `client = OpenAI()` sans clé explicite, model = `claude-sonnet-4-5` |
| **My Browser** | Accéder à l'interface Manus authentifiée | Permet de voir toutes les sessions + URLs + titres |
| **Git commit + push** | Archiver sur GitHub | Fonctionne via subprocess dans le script |

### ❌ Ce qui ne fonctionne pas

| Méthode | Problème | Alternative |
|---|---|---|
| **API `task.list` pour corpus complet** | Retourne max 200 tâches, ~89% sont des "Wide Research Subtask", ne remonte pas avant juin 2026 | → My Browser **Mac** pour scraper la liste complète |
| **My Browser depuis iOS** | Session non maintenue, page Manus se charge en mode non-connecté | → Utiliser uniquement depuis Mac |
| **My Browser dans sandbox VM** | Même problème — session perdue à chaque navigation | → Utiliser uniquement depuis Mac |
| **MCP Manus natif** | N'existe pas dans les connecteurs disponibles | → My Browser ou API directe |
| **Clé Anthropic directe** | Clé expirée/révoquée | → Utiliser le proxy sandbox OpenAI avec `client = OpenAI()` |
| **Clé OpenAI directe** | Clé externe rejetée par le proxy sandbox | → Utiliser `client = OpenAI()` sans base_url (proxy auto-configuré) |
| **Scraping HTML sidebar** | Manus est une SPA React — les sessions sont des `div[role=button]`, pas des `<a>` | → Cliquer chaque session pour récupérer l'UID depuis l'URL |

---

## 3. Marqueur d'archivage

**Format canonique :** `[✓] ` au début du titre
- Exemple : `[✓] KAP Sprint WP0-CORE-1`
- Sessions déjà archivées dans Notion (363 corpus) : certaines ont `Check ` au début (ancien format)
- **Règle de détection :** titre commence par `[✓]`, `Check `, `✓`, `✔`, `☑`, `✅`
- **Ne jamais modifier** un titre qui a déjà un marqueur

---

## 4. Prérequis avant de lancer

| Prérequis | Comment vérifier |
|---|---|
| Clé API Manus valide | `sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze` |
| Git configuré avec remote | `cd /home/ubuntu/KAP && git remote -v` |
| Proxy LLM sandbox actif | `python3 -c "from openai import OpenAI; c=OpenAI(); print('OK')"` |
| My Browser connecté (pour scraping complet) | Vérifier dans Manus Settings → Apps → My Browser |

---

## 5. Comment lancer le pipeline

### Option A — Sur une liste d'UIDs connue (rapide)

```bash
cd /home/ubuntu/KAP
python3 scripts/kap_session_archive/run_bulk_archive.py
```

Le script lit `/tmp/post_corpus_sessions.json` ou utilise l'API pour les 200 sessions récentes.

### Option B — Sur une liste d'URLs (fournie par l'utilisateur)

```bash
# Créer un fichier avec une URL par ligne
cat > /tmp/session_urls.txt << 'EOF'
https://manus.im/app/task/UID1
https://manus.im/app/task/UID2
EOF

# Extraire les UIDs et lancer
python3 -c "
import re, subprocess
with open('/tmp/session_urls.txt') as f:
    urls = f.read().splitlines()
uids = [re.search(r'/app/task/([a-zA-Z0-9]+)', u).group(1) for u in urls if '/app/task/' in u]
print(f'UIDs found: {len(uids)}')
# Puis appeler run_pipeline.py pour chaque UID
"
```

### Option C — Via My Browser (scraping complet de la sidebar)

1. S'assurer que My Browser est connecté (Settings → Apps → My Browser dans Manus)
2. Naviguer sur `https://manus.im/app`
3. Scroller la sidebar pour charger toutes les sessions
4. Extraire les UIDs en cliquant chaque session (URL = `https://manus.im/app/{UID}`)
5. Lancer le pipeline sur les UIDs collectés

---

## 6. Déduplication — règles

Le pipeline skip automatiquement une session si :
1. Le titre commence par `[✓]`, `Check `, `✓`, `✔`, `☑`, `✅`
2. Le fichier `{uid}_session_card.md` existe déjà dans `/KAP/03_Archived_Sessions/YOS/`

---

## 7. Ce que l'utilisateur doit faire manuellement

> **Pour reprendre le pipeline là où on s'est arrêté :**
> 1. Ouvre Manus sur ton **Mac** dans Chrome
> 2. Settings → Apps → My Browser → Connect
> 3. Dis à Manus : « My Browser connecté, reprends le scraping des sessions »
> 4. Manus scrape la sidebar, collecte les UIDs, lance le pipeline automatiquement
> 5. Résultat : fiches MD dans `/KAP/03_Archived_Sessions/YOS/` + titres `[✓]` dans Manus

| Action | Quand | Comment |
|---|---|---|
| Connecter My Browser | Avant scraping complet | Manus Settings → Apps → My Browser → Connect |
| Fournir liste d'URLs | Si API insuffisante | Copier-coller depuis l'interface Manus |
| Vérifier les fiches générées | Après chaque run | Voir `/KAP/03_Archived_Sessions/YOS/` ou GitHub |

---

## 8. Leçons apprises (ne pas répéter)

1. **L'API `task.list` n'est pas un corpus de sessions** — c'est un log opérationnel limité à 200 entrées récentes. Pour le corpus complet, utiliser Notion MCP (WP2-M6B) ou My Browser.
2. **Les clés LLM externes ne fonctionnent pas dans le sandbox** — toujours utiliser `client = OpenAI()` sans configuration manuelle.
3. **Manus est une SPA React** — les sessions ne sont pas des `<a>` dans le HTML. L'UID est dans l'URL après clic.
4. **Le marqueur `[✓]` est entre crochets carrés** — pas `✓` seul. Respecter ce format pour la cohérence visuelle.
5. **Ne jamais modifier le titre sans ajouter `[✓]`** — le titre est l'identifiant humain de la session.

---

## 9. Fichiers clés

| Fichier | Rôle |
|---|---|
| `scripts/kap_session_archive/run_bulk_archive.py` | Script principal bulk |
| `scripts/kap_session_archive/04_mark_archived_in_manus.py` | Mise à jour titre seule |
| `03_Archived_Sessions/YOS/` | Dossier des fiches MD |
| `03_Archived_Sessions/YOS/bulk_archive_report.json` | Rapport du dernier run |
| `/tmp/post_corpus_sessions.json` | Cache des sessions post-corpus (temporaire) |
