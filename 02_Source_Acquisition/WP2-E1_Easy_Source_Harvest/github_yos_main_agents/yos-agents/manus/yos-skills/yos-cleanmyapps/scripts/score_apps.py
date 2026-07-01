#!/usr/bin/env python3
# score_apps.py — Analyse, compare et score les apps pour identifier les doublons et les obsolètes
# Usage: python3 score_apps.py <meta_file> <output_report_md>

import sys
import os
import csv
from datetime import datetime

if len(sys.argv) < 3:
    print("Usage: python3 score_apps.py <meta_file> <output_report_md>")
    sys.exit(1)

meta_file = sys.argv[1]
output_file = sys.argv[2]

# Catégories de doublons fonctionnels définies pour Yannick
CATEGORIES = {
    "VPN": ["nordvpn", "protonvpn", "urban vpn", "speedify"],
    "Transcription/Whisper": ["macwhisper", "superwhisper", "wispr flow", "whispernotes", "whisper transcription"],
    "Productivité/Notes": ["notion", "obsidian", "heptabase", "milanote", "tana", "mem", "readwise", "mymind"],
    "Task Managers": ["todoist", "things3", "ticktick", "sorted"],
    "Browsers/Wrappers": ["vivaldi", "wavebox", "webcatalog", "google chrome", "firefox"],
    "Remote Desktop": ["screens 5", "nomachine", "splashtop", "remote desktop", "remote mouse"],
    "Video Editors": ["filmora", "handbrake", "shutter encoder", "hitpaw", "powerdirector", "davinci"],
    "Image Upscale": ["upscayl", "photo ai", "photozoom"],
    "Translation": ["mate translate", "reverso", "translatium", "translate ai", "translate now", "webtranslator"],
    "QR Code": ["qr capture", "qrcode expert", "qr factory", "qr code"]
}

apps = []

# Charger les métadonnées
with open(meta_file, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split('|')
        if len(parts) < 5:
            continue
        name, arch, last_used, size_str, path = parts
        size = int(size_str.replace('MB', ''))
        
        # Calculer le score d'obsolescence (0-100)
        # Facteurs : architecture (x86 = +30), date d'utilisation (ancienne = +50), taille (+20 si lourd et inutile)
        score = 0
        
        # Date d'utilisation
        try:
            dt = datetime.strptime(last_used, "%Y-%m-%d")
            years_unused = (datetime.now() - dt).days / 365.25
        except:
            years_unused = 10
            
        if years_unused > 3:
            score += 50
        elif years_unused > 1:
            score += 30
            
        # Arch
        if 'x86_64' in arch and 'arm64' not in arch:
            score += 30
            
        apps.append({
            "name": name,
            "arch": arch,
            "last_used": last_used,
            "size": size,
            "path": path,
            "score": score,
            "years_unused": years_unused
        })

# Identifier les doublons
doublons = {cat: [] for cat in CATEGORIES}
for app in apps:
    low_name = app["name"].lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in low_name:
                doublons[cat].append(app)
                break

# Générer le rapport Markdown
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Rapport d'Analyse yOS-CleanMyApps\n\n")
    f.write(f"Généré le : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    # Section 1 — Obsolètes (Score > 70)
    f.write("## 🔴 SECTION 1 — Apps Obsolètes (x86_64 ou inutilisées depuis +3 ans)\n\n")
    f.write("| App | Architecture | Dernière utilisation | Taille | Score Obsolescence |\n")
    f.write("|---|---|---|---|---|\n")
    obsoletes = sorted([a for a in apps if a["score"] >= 70], key=lambda x: x["score"], reverse=True)
    for app in obsoletes:
        f.write(f"| {app['name']} | {app['arch']} | {app['last_used']} | {app['size']} MB | {app['score']}/100 |\n")
    
    # Section 2 — Doublons fonctionnels
    f.write("\n## 🟡 SECTION 2 — Doublons Fonctionnels Détectés\n\n")
    for cat, d_apps in doublons.items():
        if len(d_apps) > 1:
            f.write(f"### Catégorie : {cat}\n\n")
            f.write("| App | Architecture | Dernière utilisation | Taille | Recommandation |\n")
            f.write("|---|---|---|---|---|\n")
            # Trier par date d'utilisation pour suggérer de garder la plus récente
            d_apps_sorted = sorted(d_apps, key=lambda x: x["last_used"], reverse=True)
            for i, app in enumerate(d_apps_sorted):
                rec = "⭐ GARDER (Le plus actif)" if i == 0 else "❌ SUPPRIMER (Doublon)"
                f.write(f"| {app['name']} | {app['arch']} | {app['last_used']} | {app['size']} MB | {rec} |\n")
            f.write("\n")

print(f"Rapport généré avec succès dans : {output_file}")
