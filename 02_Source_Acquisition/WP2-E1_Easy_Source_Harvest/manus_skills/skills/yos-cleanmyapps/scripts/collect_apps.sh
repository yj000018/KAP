#!/bin/bash
# collect_apps.sh — Collecte les métadonnées complètes des apps du Mac de Yannick
# Usage: ./collect_apps.sh [output_file]

OUTPUT_FILE="${1:-/tmp/apps_meta.txt}"

echo "=== Début de la collecte des apps Mac ==="
echo "Machine: $(hostname)"
echo "OS: $(sw_vers -productVersion)"
echo "Arch: $(uname -m)"

# 1. Lister les apps système et utilisateur
find /Applications -maxdepth 1 -name "*.app" > /tmp/apps_list.txt
find /Applications/Setapp -maxdepth 1 -name "*.app" 2>/dev/null >> /tmp/apps_list.txt

echo "Total apps trouvées: $(wc -l < /tmp/apps_list.txt)"

# 2. Extraire les métadonnées pour chaque app
echo "Extraction des métadonnées (nom, architecture, dernière utilisation, taille)..."
> "$OUTPUT_FILE"

while read -r app_path; do
  [ -z "$app_path" ] && continue
  app_name=$(basename "$app_path" .app)
  
  # Taille
  size=$(du -sm "$app_path" 2>/dev/null | cut -f1)
  [ -z "$size" ] && size=0
  
  # Dernière utilisation (atime)
  last_used=$(stat -f "%Sa" -t "%Y-%m-%d" "$app_path" 2>/dev/null)
  [ -z "$last_used" ] && last_used="1970-01-01"
  
  # Architecture (x86_64, arm64, Universal)
  exec_path="$app_path/Contents/MacOS/"*
  arch="Unknown"
  if [ -d "$app_path/Contents/MacOS" ]; then
    arch=$(lipo -archs "$app_path/Contents/MacOS/"* 2>/dev/null | head -1)
  fi
  [ -z "$arch" ] && arch="Unknown"
  
  # Écrire dans le fichier
  echo "$app_name|$arch|$last_used|${size}MB|$app_path" >> "$OUTPUT_FILE"
done < /tmp/apps_list.txt

echo "=== Collecte terminée ==="
echo "Métadonnées sauvegardées dans : $OUTPUT_FILE"
