#!/usr/bin/env bash
set -e

declare -A files=(
  [rotmod_files]="https://zenodo.org/records/15691753/files/rotmod_files.rar?download=1"
  [DH_data]="https://zenodo.org/records/15691765/files/DH_data.rar?download=1"
)

for dir in "${!files[@]}"; do
  url="${files[$dir]}"
  mkdir -p "$dir"
  curl -sSL "$url" -o "$dir/${dir}.rar"
  # 解压到对应目录
  7z x "$dir/${dir}.rar" -o"$dir" > /dev/null
done
