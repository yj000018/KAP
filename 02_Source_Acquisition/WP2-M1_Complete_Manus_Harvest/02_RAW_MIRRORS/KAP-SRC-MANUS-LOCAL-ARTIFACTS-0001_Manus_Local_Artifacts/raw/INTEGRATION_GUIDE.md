# Session Navigator - AI Clustering Integration Guide

## Vue d'ensemble

Ce guide explique comment intégrer la fonctionnalité de clustering AI semi-automatique dans le TreeView existant de yOS.

**Objectif** : Permettre la sélection de sessions, l'analyse AI pour détecter les clusters thématiques, et la validation manuelle avant fusion.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     TreeView UI (Existant)                   │
│  - Sélection multi-sessions                                  │
│  - Affichage hiérarchique                                    │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              Bouton "Analyze for Merge" (Nouveau)            │
│  - Envoie session_ids sélectionnés à l'API                   │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│            API de Clustering (Backend Python)                │
│  - Chroma Vector DB (similarité sémantique)                  │
│  - LLM (GPT-4) pour analyse et rationale                     │
│  - Retourne clusters proposés + outliers                     │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│          Panneau de Validation (Nouveau)                     │
│  - Affiche clusters proposés avec confidence                 │
│  - Bouton "Merge" par cluster                                │
│  - Affiche outliers (sessions non groupées)                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Composants Livrés

### 1. Backend API de Clustering

**Fichier** : `/home/ubuntu/skills/session-navigator/scripts/clustering_api.py`

**Fonctionnalités** :
- Endpoint : `POST http://localhost:5001/api/analyze-for-merge`
- Input : `{ "session_ids": ["id1", "id2", ...] }`
- Output : Clusters proposés avec confidence, rationale, et outliers

**Démarrage** :
```bash
cd /home/ubuntu/skills/session-navigator/scripts
python3 clustering_api.py
```

**Dépendances** :
- chromadb
- flask
- flask-cors
- openai (ou autre LLM)

---

### 2. Script d'Indexation Chroma

**Fichier** : `/home/ubuntu/skills/session-navigator/scripts/ai_clustering.py`

**Fonctionnalités** :
- Indexe les sessions dans Chroma Vector DB
- Calcule la similarité sémantique
- Clustering hiérarchique

**Usage** :
```python
from ai_clustering import cluster_sessions

clusters = cluster_sessions(session_ids, similarity_threshold=0.75)
```

---

### 3. Données de Test

**Fichier** : `/home/ubuntu/test_sessions_data.json`

Format JSON compatible avec le TreeView :
```json
[
  {
    "key": "category-conversations",
    "title": "📝 Conversation Archive",
    "type": "category",
    "children": [
      {
        "key": "session-id",
        "title": "Session Title",
        "type": "session",
        "metadata": {
          "url": "https://manus.im/share/...",
          "id": "session-id"
        }
      }
    ]
  }
]
```

---

## Étapes d'Intégration

### Étape 1 : Ajouter le Bouton "Analyze for Merge"

**Dans le TreeView existant**, ajouter un bouton dans la toolbar :

```typescript
// Dans le composant TreeView
<Button
  variant="default"
  onClick={handleAnalyzeForMerge}
  disabled={selectedIds.length < 2}
>
  <Sparkles className="h-4 w-4 mr-2" />
  Analyze for Merge ({selectedIds.length})
</Button>
```

**Handler** :
```typescript
const handleAnalyzeForMerge = async () => {
  if (selectedIds.length < 2) {
    toast.error('Sélectionnez au moins 2 sessions');
    return;
  }

  setIsAnalyzing(true);

  try {
    const response = await fetch('http://localhost:5001/api/analyze-for-merge', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_ids: selectedIds })
    });

    const result = await response.json();
    setClusterResult(result);
    toast.success('Analyse terminée !');
  } catch (error) {
    toast.error('Erreur : ' + error.message);
  } finally {
    setIsAnalyzing(false);
  }
};
```

---

### Étape 2 : Ajouter le Panneau de Résultats

**Créer un nouveau composant** `ClusterResultsPanel.tsx` :

```typescript
interface ClusterResultsPanelProps {
  result: ClusterResult | null;
  onMergeCluster: (cluster: Cluster) => void;
}

export function ClusterResultsPanel({ result, onMergeCluster }: ClusterResultsPanelProps) {
  if (!result) {
    return (
      <div className="flex flex-col items-center justify-center h-full">
        <Sparkles className="h-16 w-16 text-muted-foreground/30 mb-4" />
        <p className="text-sm text-muted-foreground">
          Sélectionnez des sessions et cliquez sur "Analyze for Merge"
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6 p-6">
      {/* Summary */}
      <div>
        <h3 className="text-lg font-semibold mb-2">Analyse</h3>
        <p className="text-sm text-muted-foreground">
          {result.analysis_summary}
        </p>
      </div>

      {/* Clusters */}
      <div>
        <h3 className="text-lg font-semibold mb-4">Clusters Proposés</h3>
        {result.clusters.map((cluster, idx) => (
          <Card key={idx} className="p-4 mb-4">
            <div className="flex items-start justify-between mb-3">
              <div>
                <h4 className="font-semibold">{cluster.name}</h4>
                <p className="text-xs text-muted-foreground">
                  Confidence: {cluster.confidence}%
                </p>
              </div>
              <Button
                size="sm"
                onClick={() => onMergeCluster(cluster)}
              >
                Merge
              </Button>
            </div>
            <p className="text-sm text-muted-foreground mb-3">
              {cluster.rationale}
            </p>
            <div className="space-y-1">
              {cluster.sessions.map((session) => (
                <div key={session.id} className="text-xs p-2 rounded bg-muted/50">
                  {session.title}
                </div>
              ))}
            </div>
          </Card>
        ))}
      </div>

      {/* Outliers */}
      {result.outliers.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold mb-2">Outliers</h3>
          <p className="text-sm text-muted-foreground mb-2">
            Sessions ne correspondant à aucun cluster :
          </p>
          {result.outliers.map((id) => (
            <div key={id} className="text-xs p-2 rounded bg-muted/50 mb-1">
              {id}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

---

### Étape 3 : Intégrer dans le Layout

**Modifier la page principale** pour afficher le panneau de résultats à côté du TreeView :

```typescript
<div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
  {/* TreeView (existant) */}
  <Card className="h-[calc(100vh-12rem)]">
    <SessionTreeView
      data={treeData}
      onSelectionChange={setSelectedIds}
    />
  </Card>

  {/* Panneau de Résultats (nouveau) */}
  <Card className="h-[calc(100vh-12rem)] overflow-auto">
    <ClusterResultsPanel
      result={clusterResult}
      onMergeCluster={handleMergeCluster}
    />
  </Card>
</div>
```

---

### Étape 4 : Implémenter la Fusion

**Handler de fusion** :

```typescript
const handleMergeCluster = async (cluster: Cluster) => {
  // 1. Créer une MASTER SESSION
  const masterSessionTitle = cluster.name.toUpperCase();
  
  // 2. Appeler le script de fusion
  const response = await fetch('http://localhost:5001/api/merge-sessions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      session_ids: cluster.session_ids,
      master_title: masterSessionTitle
    })
  });

  const result = await response.json();
  
  // 3. Afficher le résultat
  toast.success(`Master session créée : ${result.master_session_url}`);
  
  // 4. Archiver les sessions sources
  // TODO: Implémenter l'archivage
};
```

---

## Configuration

### Variables d'Environnement

Créer un fichier `.env` dans le projet TreeView :

```bash
# API de Clustering
VITE_CLUSTERING_API_URL=http://localhost:5001

# OpenAI (pour LLM)
OPENAI_API_KEY=your_openai_key

# Chroma DB
CHROMA_DB_PATH=/home/ubuntu/.chroma_db
```

---

## Tests

### Test 1 : Sélection et Analyse

1. Charger les données de test (`test_sessions_data.json`)
2. Sélectionner 4 sessions
3. Cliquer sur "Analyze for Merge"
4. Vérifier que les clusters s'affichent

**Résultat attendu** :
- 2-3 clusters proposés
- Confidence > 70%
- Outliers identifiés

---

### Test 2 : Validation et Fusion

1. Sélectionner un cluster proposé
2. Cliquer sur "Merge"
3. Vérifier la création de la MASTER SESSION

**Résultat attendu** :
- MASTER SESSION créée avec titre en MAJUSCULES
- Sessions sources archivées
- Liens bidirectionnels préservés

---

## Déploiement

### Backend API

**Option 1 : Local (développement)**
```bash
python3 clustering_api.py
```

**Option 2 : Production (Docker)**
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "clustering_api.py"]
```

### Frontend

**Intégrer dans le projet Manus existant** :
1. Ouvrir le projet TreeView dans Manus
2. Ajouter les fichiers modifiés
3. Créer un checkpoint
4. Tester via Preview

---

## Maintenance

### Mise à Jour du Modèle de Clustering

Pour améliorer la qualité du clustering :

1. **Ajuster le seuil de similarité** :
   ```python
   # Dans ai_clustering.py
   SIMILARITY_THRESHOLD = 0.80  # Augmenter pour clusters plus stricts
   ```

2. **Améliorer les prompts LLM** :
   ```python
   # Dans clustering_api.py
   prompt = f"""
   Analyze these {len(session_ids)} sessions and propose thematic clusters.
   
   Focus on:
   - Technical vs conceptual content
   - Implementation vs planning
   - Data layer vs UI layer
   
   Be strict: only group sessions with >85% thematic overlap.
   """
   ```

3. **Enrichir les métadonnées** :
   - Ajouter tags depuis Notion
   - Extraire keywords automatiquement
   - Analyser les timestamps pour détecter les séquences

---

## Troubleshooting

### Problème : API ne répond pas

**Solution** :
```bash
# Vérifier que l'API tourne
ps aux | grep clustering_api

# Voir les logs
tail -f /tmp/clustering_api.log

# Redémarrer
pkill -f clustering_api
python3 clustering_api.py
```

### Problème : Clusters de mauvaise qualité

**Solution** :
1. Vérifier que les sessions sont bien indexées dans Chroma
2. Augmenter le seuil de similarité
3. Enrichir les descriptions de sessions

### Problème : CORS errors

**Solution** :
```python
# Dans clustering_api.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

---

## Roadmap

### v1.1 (Actuel)
- ✅ Clustering semi-automatique
- ✅ Validation manuelle
- ✅ API de clustering

### v1.2 (Prochaine)
- [ ] Fusion automatique programmée (1x/semaine)
- [ ] Détection de sessions similaires en temps réel
- [ ] Suggestions proactives de fusion

### v1.3 (Future)
- [ ] Clustering multi-niveaux (projets → sessions → messages)
- [ ] Analyse temporelle (détecter séquences de sessions)
- [ ] Export vers Notion automatique

---

## Références

- **Chroma DB** : https://docs.trychroma.com/
- **OpenAI API** : https://platform.openai.com/docs/api-reference
- **Manus Webdev** : https://open.manus.im/docs/web-development

---

## Support

Pour toute question ou problème :
1. Consulter les logs : `/tmp/clustering_api.log`
2. Vérifier la documentation Chroma
3. Tester avec les données de test fournies

---

**Version** : 1.0  
**Date** : 2026-02-15  
**Auteur** : yOS Session Navigator Team
