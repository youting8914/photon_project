#!/usr/bin/env bash
set -e

declare -A files=(
  [rotmod_files]="hhttps://zenodo.org/records/15691753/files/rotmod_files.rar?download=1"
  [extra_data]="https://zenodo.org/record/1234567/files/extra_data.zip?download=1"

  # 如果后续还有，继续在这里添加 key=url
)

for dir in "${!files[@]}"; do
  url="${files[$dir]}"
  mkdir -p "$dir"
  wget -O "$dir/${dir}.zip" "$url"
  unzip -o "$dir/${dir}.zip" -d "$dir"
done
