#!/usr/bin/env bash
set -e

declare -A files=(
  [rotmod_files]="https://zenodo.org/records/15691753/files/rotmod_files.rar?download=1"
  [DH_data]="https://zenodo.org/api/records/15691765/draft/files/DH_data.rar/content"

  # 如果后续还有，继续在这里添加 key=url
)

for dir in "${!files[@]}"; do
  url="${files[$dir]}"
  mkdir -p "$dir"
  wget -O "$dir/${dir}.zip" "$url"
  unzip -o "$dir/${dir}.zip" -d "$dir"
done
