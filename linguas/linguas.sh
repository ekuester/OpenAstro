#!/bin/bash
# start in directory 'linguas'
linguas="./LINGUAS"
cd ../locale
IFS=$'\n'
for lingua in `cat $linguas`; do
  [[ "$lingua" =~ ^#.*$ ]] && continue
  echo "$lingua.po read from $linguas"
  rm -frv $lingua
  mkdir -p "$lingua/LC_MESSAGES"
  msgfmt ./$lingua.po -o "$lingua/LC_MESSAGES/openastro.mo"
  echo "./$lingua/LC_MESSAGES/openastro.mo generated"
done
