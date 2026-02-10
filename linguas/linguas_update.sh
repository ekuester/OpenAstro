#!/bin/bash
# start in directory 'linguas'
linguas="./LINGUAS"
cd ../locale
IFS=$'\n'
for lingua in `cat $linguas`; do
  [[ "$lingua" =~ ^#.*$ ]] && continue
  echo "$lingua.po read from $linguas"
  msgmerge --update ./$lingua/LC_MESSAGES/openastro.po ./templates/openastro.pot
  echo "./$lingua/LC_MESSAGES/openastro.po updated"
done

