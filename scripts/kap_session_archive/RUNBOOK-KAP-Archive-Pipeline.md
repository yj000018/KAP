# KAP Archive Pipeline — Runbook Technique & Procédural

**Version:** 1.1 — 2026-07-02
**Auteur:** Manus (documenté après 3 cycles d'apprentissage et de trial-and-error)
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

## ⚠️ RÈGLE CRITIQUE — Extraction des UIDs (Procédure Définitive)

> **Problème fondamental :** L'API `task.list` de Manus est limitée aux 200 dernières tâches (et remplie de bruit "Wide Research Subtask"). Pour archiver **toutes** les sessions historiques, il faut extraire les UIDs directement depuis l'interface web de Manus.
>
> **Contrainte My Browser :** My Browser dans le sandbox Manus (machine virtuelle) ne maintient pas la session authentifiée. My Browser depuis iOS perd la session.
>
> **La SEULE méthode fiable est une extraction manuelle via la console JS sur Chrome Mac.** Ne plus jamais tenter d'automatiser cette étape avec Playwright ou My Browser Sandbox.

### Procédure pas-à-pas pour l'utilisateur (À copier-coller quand on demande les UIDs)

**Prérequis :** Être sur **Mac** et utiliser **Google Chrome**.

1. Ouvre Chrome sur ton Mac et va sur `https://manus.im/app`
2. Dans la barre latérale de gauche (sidebar), scrolle **manuellement jusqu'en bas** pour charger tout l'historique (Manus utilise du virtual/lazy loading, il faut tout charger dans le DOM).
3. Ouvre les outils de développement (Console) :
   - Fais un clic droit n'importe où → **Inspecter** (Inspect)
   - Clique sur l'onglet **Console**
4. Copie et colle **exactement** ce script JS dans la console et appuie sur Entrée :

```javascript
// Script d'extraction des UIDs et Titres Manus (v1.2) - FIX REACT SPA
// Manus est une SPA React sans balises <a> pour les sessions. 
// Ce script extrait l'état React sous-jacent contenant l'historique complet.

let sessions = [];

// Méthode 1: Chercher dans les props React des éléments de la sidebar
const sidebarItems = Array.from(document.querySelectorAll('div[role="button"]'));
for (let el of sidebarItems) {
    let title = el.innerText.trim().split('\n')[0];
    const skip = ['New task', 'Agent', 'Plugins', 'Scheduled', 'Library', 'Projects', 'Tasks'];
    if (!title || skip.includes(title) || title.length < 5) continue;
    
    // Essayer de trouver l'UID dans les attributs React internes
    let uid = null;
    for (let key in el) {
        if (key.startsWith('__reactProps')) {
            try {
                // Navigation profonde dans l'arbre des props React pour trouver l'ID
                let props = el[key];
                if (props.children && props.children.props && props.children.props.task) {
                    uid = props.children.props.task.id;
                } else if (props.onClick) {
                    // Parfois l'ID est bindé dans le onClick handler
                    let fnStr = props.onClick.toString();
                    let match = fnStr.match(/([a-zA-Z0-9]{20,})/);
                    if (match) uid = match[1];
                }
            } catch(e) {}
        }
    }
    
    if (uid) {
        sessions.push(uid + " | " + title);
    } else {
        // Fallback: on garde le titre sans UID pour analyse
        sessions.push("MISSING_UID | " + title);
    }
}

// Si la méthode 1 échoue, Méthode 2: Extraction via l'API fetch interceptée
if (sessions.filter(s => !s.startsWith("MISSING_UID")).length === 0) {
    console.log("⚠️ UIDs introuvables dans le DOM React. Utilisation du Network tab requise.");
    console.log("Veuillez rafraîchir la page avec l'onglet Network ouvert, filtrer sur 'task.list', et copier la réponse JSON.");
}

let uniqueSessions = [...new Set(sessions)];

console.log("=== COPIEZ TOUT CE QUI SUIT ET COLLEZ-LE DANS MANUS ===");
console.log(uniqueSessions.join('\n'));
console.log("=== FIN DE LA LISTE (" + uniqueSessions.length + " sessions trouvées) ===");
```

5. Sélectionne tout le texte affiché entre les lignes `=== COPIEZ... ===` et `=== FIN... ===`, copie-le.
6. Colle-le directement dans notre conversation Manus.
7. Je prendrai le relais pour filtrer celles qui n'ont pas de `[✓]` et lancerai le pipeline d'archivage en bulk.

---

## 2. Ce qui fonctionne — ce qui ne fonctionne pas

### ✅ Ce qui fonctionne

| Méthode | Usage | Notes |
|---|---|---|
| **API `task.listMessages`** | Récupérer le contenu d'une session par UID | Fonctionne bien, paramètre = `task_id` |
| **API `task.update`** | Modifier le titre d'une session | Fonctionne — payload `{"task_id": uid, "title": "nouveau titre"}` |
| **Extraction Console JS** | Obtenir la liste complète des UIDs | **LA SEULE MÉTHODE FIABLE** pour l'historique complet. |
| **LLM proxy sandbox** | Générer les fiches MD | Utiliser `client = OpenAI()` sans clé explicite, model = `claude-sonnet-4-5` ou `claude-sonnet-4-6` |
| **Git commit + push** | Archiver sur GitHub | Fonctionne via subprocess dans le script |

### ❌ Ce qui ne fonctionne pas (Ne plus essayer)

| Méthode | Problème | Alternative |
|---|---|---|
| **API `task.list` pour corpus complet** | Retourne max 200 tâches, rempli de sous-tâches. | → Console JS Chrome Mac |
| **My Browser depuis iOS** | Session non maintenue. | → Chrome Mac |
| **My Browser dans sandbox VM** | Session perdue à chaque navigation. | → Console JS Chrome Mac |
| **Playwright Python (Sandbox)** | Pas de port CDP exposé pour My Browser, login impossible. | → Console JS Chrome Mac |
| **Script JS avec `copy()`** | La fonction `copy()` du navigateur échoue souvent silencieusement pour de gros volumes. | → Utiliser `console.log()` et copier manuellement. |
| **Clés Anthropic/OpenAI directes** | Rejetées ou expirées dans le sandbox. | → Utiliser le proxy sandbox OpenAI. |

---

## 3. Marqueur d'archivage

**Détection :** Le check peut être **au début OU à la fin** du titre — les deux sont acceptés comme « déjà archivé ».

**Convention :** On ajoute toujours le check **au début** du titre pour les nouvelles archives.

**Format canonique :** `[✓] ` au début du titre
- Exemple : `[✓] KAP Sprint WP0-CORE-1`
- **Règle de détection :** titre commence par `[✓]`, `Check `, `✓`, `✔`, `☑`, `✅`
- **Ne jamais modifier** un titre qui a déjà un marqueur.

---

## 4. Prérequis avant de lancer le Pipeline (Côté Agent)

| Prérequis | Comment vérifier |
|---|---|
| Clé API Manus valide | Stockée dans `/home/ubuntu/KAP/.env` (var `MANUS_API_KEY`) — **JAMAIS dans le code** |
| Créer une nouvelle clé si 401 | `https://manus.im/app?show_settings=integrations&app_name=api` → `+ Create new` → sans expiration → stocker dans `.env` + 1Password |
| Clé actuelle | `KAP-Pipeline-Permanent` — créée 2026-07-02 — voir `.env` local |
| Git configuré avec remote | `cd /home/ubuntu/KAP && git remote -v` |
| Proxy LLM sandbox actif | `python3 -c "from openai import OpenAI; c=OpenAI(); print('OK')"` |
| Fichier UIDs prêt | Un fichier texte avec une liste d'UIDs extraits par l'utilisateur. |

---

## 5. Comment lancer le pipeline en Bulk

Une fois que l'utilisateur a collé la liste issue de la console JS (format `UID | Titre`) :

1. Sauvegarder le texte collé dans un fichier, ex: `/tmp/raw_sessions.txt`
2. Extraire uniquement les UIDs des sessions qui n'ont pas le marqueur `[✓]`
3. Créer un fichier `/tmp/uids_to_archive.txt` contenant un UID par ligne
4. Lancer le script de bulk archive (qui doit être adapté pour lire ce fichier) :

```bash
# Exemple de script python rapide pour lancer le pipeline sur la liste d'UIDs
python3 << 'EOF'
import os, subprocess

with open('/tmp/uids_to_archive.txt', 'r') as f:
    uids = [line.strip() for line in f if line.strip()]

print(f"Lancement du pipeline pour {len(uids)} sessions...")

for i, uid in enumerate(uids, 1):
    print(f"\n--- [{i}/{len(uids)}] Traitement de {uid} ---")
    cmd = ["python3", "/home/ubuntu/KAP/scripts/kap_session_archive/run_pipeline_enhanced.py", uid]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Succès pour {uid}")
    else:
        print(f"❌ Échec pour {uid}:\n{result.stderr}")
EOF
```

---

## 6. Déduplication — règles (Rappel)

Le script `run_pipeline_enhanced.py` skip automatiquement une session si :
1. Le titre commence par `[✓]`, `Check `, `✓`, `✔`, `☑`, `✅`
2. Le fichier `{uid}_factsheet.md` (ou `_session_card.md`) existe déjà dans `/KAP/03_Archived_Sessions/YOS/`

---

## 7. Fichiers clés

| Fichier | Rôle |
|---|---|
| `scripts/kap_session_archive/run_pipeline_enhanced.py` | Pipeline v3 (YAML + Card + Verbatim) |
| `scripts/kap_session_archive/run_bulk_archive.py` | Script principal bulk (à adapter pour lire liste UIDs) |
| `03_Archived_Sessions/YOS/` | Dossier des fiches MD |
