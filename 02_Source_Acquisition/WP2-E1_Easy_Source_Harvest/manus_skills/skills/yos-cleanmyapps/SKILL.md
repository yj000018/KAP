---
name: yos-cleanmyapps
description: Workflow structuré et réutilisable pour auditer, nettoyer et optimiser les applications installées sur macOS. Permet de maintenir une liste d'applications saine, consistante et synergétique en identifiant les doublons fonctionnels, les obsolètes x86_64 et les apps superseded par macOS.
---

# yOS-CleanMyApps 🧠🧹

Ce skill fournit un protocole robuste pour auditer, nettoyer et maintenir un écosystème d'applications optimal sur macOS, en éliminant les redondances et en privilégiant des solutions "1 app pro majeure" par objectif.

## Principes Directeurs (yOS-Standard)

1. **L'Économie Cognitive & Token** : Moins d'apps = moins de bruit, moins de processus en arrière-plan, plus de clarté pour l'IA opératrice.
2. **La Synergie "1 App Majeure"** : Pour chaque besoin (Notes, Task Manager, VPN), identifier et garder le leader absolu (souvent couvert par un abonnement global comme **Setapp**), et éliminer sans pitié les alternatives marginales.
3. **Fidélité & Numérotation** : Toute liste d'apps générée pour décision utilisateur doit être **systématiquement numérotée** pour permettre des retours rapides (ex: "Supprime 3, 7, 12").

---

## Workflow d'Exécution

Le workflow se compose de 3 phases exécutées de manière autonome par Manus via le Desktop Client.

### Phase 1 : Collecte des Métadonnées (`collect_apps.sh`)
Exécuter le script de collecte pour extraire la liste brute des apps avec leur architecture (arm64 vs x86_64), leur date de dernière utilisation (atime) et leur taille sur le disque.

```bash
bash /home/ubuntu/skills/yos-cleanmyapps/scripts/collect_apps.sh /tmp/apps_meta.txt
```

### Phase 2 : Analyse et Scoring (`score_apps.py`)
Analyser les données collectées pour classifier les apps selon deux axes :
1. **Obsolescence** : Score calculé sur l'absence de version native ARM64 et l'inactivité prolongée (> 3 ans).
2. **Doublons fonctionnels** : Regroupement par catégories (VPN, Transcription, Task Managers, etc.) pour comparaison directe.

```bash
python3 /home/ubuntu/skills/yos-cleanmyapps/scripts/score_apps.py /tmp/apps_meta.txt /tmp/apps_report.md
```

### Phase 3 : Présentation et Décision
Présenter à l'utilisateur un rapport structuré et **numéroté** divisé en :
- **🔴 PRIORITÉ 1** : Apps obsolètes x86_64 inutilisées (Suppression sans risque).
- **🟡 PRIORITÉ 2** : Doublons fonctionnels avec recommandation claire "Garder vs Supprimer" basée sur l'usage réel et les licences actives (ex: Setapp).
- **🔵 PRIORITÉ 3** : Apps superseded par des fonctions natives de macOS Sequoia.

---

## Protocole de Suppression Sécurisée

Lors de la suppression des apps validées par l'utilisateur :

1. **Vérifier l'ownership** : Les apps App Store appartiennent à `root` et nécessitent des privilèges administrateur.
2. **Utiliser le mot de passe mémorisé** : Si l'utilisateur a configuré son mot de passe administrateur dans la session (ex: 4 espaces), l'utiliser via `sudo -S` :
   ```bash
   printf '    ' | sudo -S rm -rf "/Applications/TargetApp.app"
   ```
3. **Alternative Finder** : Si `sudo` échoue ou n'est pas configuré, utiliser `osascript` pour envoyer l'app vers la Corbeille via l'interface Finder :
   ```bash
   osascript -e 'tell application "Finder" to delete POSIX file "/Applications/TargetApp.app"'
   ```
4. **Vider la Corbeille de manière sécurisée** :
   ```bash
   osascript -e 'tell application "Finder" to empty trash'
   ```

---

## Catégories de Référence & Leaders Recommandés (yOS)

| Catégorie | Leader Recommandé | Raison / Alternative |
|---|---|---|
| **VPN** | **NordVPN** ⭐ | Licencié / Supprimer Proton, Urban, Speedify |
| **Transcription** | **superwhisper** ⭐ (Setapp) | Dictée live. **MacWhisper** pour les fichiers audio |
| **Notes / PKM** | **Obsidian** / **Notion** ⭐ | Centralisation / Supprimer Mem, Tana, mymind |
| **Task Manager** | **Todoist** ⭐ | Multi-plateforme / Supprimer TickTick, Things3 |
| **Browser** | **Wavebox** ⭐ | Workspaces pro / Supprimer WebCatalog |
| **Screenshot** | **CleanShot X** ⭐ (Setapp) | Inégalé / Supprimer Lightshot |
| **AirPlay** | **macOS Sequoia Natif** ⭐ | Intégration système / Supprimer JustStream, Reflector |
