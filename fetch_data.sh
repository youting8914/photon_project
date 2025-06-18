#!/usr/bin/env bash
set -e

declare -A files=(
  [rotmod_files]="https://zenodo.org/records/15691753/files/rotmod_files.rar?download=1"
  [DH_data]="https://zenodo.org/api/records/15691765/draft/files/DH_data.rar/content"
)

for dir in "${!files[@]}"; do
  url="${files[$dir]}"
  mkdir -p "$dir"
  wget -O "$dir/${dir}.rar" "$url"
  # 用 7z 解压 RAR 到对应目录
  7z x "$dir/${dir}.rar" -o"$dir"
done
