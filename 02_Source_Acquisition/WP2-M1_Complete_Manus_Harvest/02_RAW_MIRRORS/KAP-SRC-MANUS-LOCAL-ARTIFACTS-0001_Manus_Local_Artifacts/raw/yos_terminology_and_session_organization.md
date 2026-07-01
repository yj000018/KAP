# yOS : Terminologie Canonique et Organisation des Sessions

## 1. Distinction Terminologique Fondamentale

Pour assurer une compréhension et une collaboration parfaites entre Yannick et Manus dans le contexte de **yOS (Yannick Operating System)**, la terminologie suivante est adoptée comme canonique. Elle prime sur la terminologie par défaut de Manus.

| Terme yOS | Définition Canonique | Terme Manus Équivalent |
| :--- | :--- | :--- |
| **Session** | Une interaction complète et cohérente entre Yannick et Manus, du début à la fin. | `Task` |
| **Task** | Un item actionnable, une tâche à faire (todo item) découlant d'une session ou d'une réflexion. | N/A |

**Implication :** Manus doit systématiquement utiliser les termes "Session" et "Task" selon leur définition yOS dans toutes les communications et documentations relatives à yOS.

## 2. Organisation des Sessions : État Actuel et Recommandations

### 2.1. Constat

L'interface Manus ne propose **aucune fonctionnalité native** pour organiser les sessions. Il n'existe pas de système de :
- **Projets**
- **Dossiers (Folders)**
- **Tags**

Chaque session est une entité isolée, ce qui rend difficile le suivi et le regroupement thématique des interactions.

### 2.2. Solution de Contournement (Workaround)

La seule méthode actuelle pour organiser les sessions repose sur le skill **`memory-manager`**, qui utilise une base de données Notion ("🧠 Manus Memory Hub").

Le processus est le suivant :
1.  Une session est terminée.
2.  L'utilisateur demande l'archivage de la session via la commande `"Archive cette conversation"`.
3.  Manus crée une entrée de type `📝 Conversation Archive` dans Notion.
4.  Cette entrée peut à son tour àtre liée à une page de type `🎯 Projet / Thème`.

**Limites de cette approche :**
- **Réactive et non pro-active :** L'organisation se fait *après* la session, pas avant ou pendant.
- **Manuelle :** Nécessite une action explicite de l'utilisateur pour chaque session.
- **Dépendance externe :** Repose entièrement sur Notion.

### 2.3. Recommandation : Demande de Fonctionnalité Native

Pour répondre au besoin structurel d'organisation, la création d'une fonctionnalité native dans Manus est la solution la plus robuste.

**Objectif :** Permettre de créer et d'assigner des sessions à des **Projets**, de les organiser avec des **Tags** et de les regrouper dans des **Dossiers** directement depuis l'interface Manus.

**Action recommandée :**
Soumettre une demande de fonctionnalité (feature request) détaillée à l'équipe de développement de Manus.

- **Lien pour la soumission :** [https://help.manus.im](https://help.manus.im)
