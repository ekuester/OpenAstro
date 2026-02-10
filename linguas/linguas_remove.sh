#!/bin/bash
# start in directory 'linguas'
linguas="./LINGUAS"
cd ../locale
IFS=$'\n'
for lingua in `cat $linguas`; do
  [[ "$lingua" =~ ^#.*$ ]] && continue
  echo "$lingua.mo read from $linguas"
  rm -fv ./$lingua/LC_MESSAGES/openastro.mo
  echo "./$lingua/LC_MESSAGES/openastro.mo deleted"
done

