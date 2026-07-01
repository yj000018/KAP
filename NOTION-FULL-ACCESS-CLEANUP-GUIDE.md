# Notion — FULL ACCESS Cleanup Guide
**Objectif :** 2 workspaces propres, 2 intégrations actives (MANUS + ChatGPT), zéro confusion.

---

## Résultat de l'audit (maintenant)

| Token | Bot | Workspace | Sessions DB | Statut |
|---|---|---|---|---|
| `ntn_144641...` | MANUS | **Y-world** (kjimene648) | ✅ UNBLOCKED | **KEEPER — c'est lui** |
| `ntn_394915...` | YOS Comet-Light | Yannick (legacy) | ❌ 0 accès | **À SUPPRIMER** |

**Sessions DB est maintenant débloquée.** Le FULL ACCESS fonctionne.

---

## Architecture cible

```
Y-world (kjimene648@student.glendale.edu)  ← WORKSPACE PROFESSIONNEL yOS/KOSMO
  └── Intégration MANUS        → FULL ACCESS ✅ (déjà actif)
  └── Intégration ChatGPT      → FULL ACCESS (à configurer, voir ci-dessous)

Yannick (yannick.jolliet@gmail.com)        ← WORKSPACE PERSO (tests, perso, inutilisé)
  └── Aucune intégration active (nettoyer)
```

---

## Plan d'action — 3 étapes (15 min total)

### ÉTAPE 1 — Nettoyer le workspace "Yannick" (perso)
> Durée : 3 min

1. Ouvre Notion, bascule sur le workspace **Yannick** (yannick.jolliet@gmail.com)
2. Va dans **Settings** > **My connections**
3. Supprime toutes les intégrations : YOS Comet-Light, Manus 2, et toute autre
4. Ce workspace reste vide d'intégrations — c'est voulu

---

### ÉTAPE 2 — Nettoyer le workspace "Y-world" (pro)
> Durée : 5 min

1. Bascule sur le workspace **Y-world** (kjimene648)
2. Va dans **Settings** > **My connections**
3. **Garde UNIQUEMENT :** l'intégration **MANUS** (déjà configurée, FULL ACCESS actif)
4. **Supprime :** toutes les autres intégrations inutiles (Manus 2, vieilles OAuth, etc.)
5. Vérifie que MANUS a bien le niveau d'accès **"All workspace pages"** (pas "Selected pages")

---

### ÉTAPE 3 — Ajouter ChatGPT en FULL ACCESS sur Y-world
> Durée : 5 min

ChatGPT utilise une intégration OAuth Notion officielle. Voici comment :

1. Dans ChatGPT, va dans **Settings** > **Connected Apps** (ou via un GPT qui demande Notion)
2. Connecte ton compte Notion — **sélectionne le workspace Y-world** (kjimene648)
3. Quand Notion demande quelles pages partager, sélectionne **"All pages"** ou le dossier racine
4. Confirme

> **Attention :** ChatGPT utilise une OAuth publique, pas un token interne. Le token est géré côté OpenAI — tu n'as pas à le stocker manuellement.

---

## Ce que ça donne après nettoyage

| Workspace | Usage | Intégrations actives |
|---|---|---|
| **Y-world** (pro) | yOS, KOSMO, Manus Memory, KAP, tout | MANUS ✅ + ChatGPT ✅ |
| **Yannick** (perso) | Tests perso, notes privées | Aucune |

**Tokens à conserver (1 seul) :**
```
MANUS Y-world: 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
```

**Tokens à archiver/supprimer :**
```
YOS Comet-Light (legacy): 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 → OBSOLÈTE
```

---

## Validation finale (je peux tester moi-même)
Une fois les étapes faites, je re-teste les deux tokens et confirme l'état propre.
