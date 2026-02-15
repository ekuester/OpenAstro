#!/bin/bash
# start in directory 'linguas'
cd ../locale
linguas="../linguas/LINGUAS"
IFS=$'\n'
for lingua in `cat $linguas`; do
  [[ "$lingua" =~ ^#.*$ ]] && continue
  echo "$lingua.po read from $linguas"
  msgfmt ./$lingua/LC_MESSAGES/openastro.po -o ./$lingua/LC_MESSAGES/openastro.mo
  echo "./$lingua/LC_MESSAGES/openastro.mo generated"
done

