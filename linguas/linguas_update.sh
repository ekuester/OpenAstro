#!/bin/bash
# get filename as parameter $1 from command line e.g. openastro or astroChart
# start in directory 'linguas'
cd ../locale
linguas="../linguas/LINGUAS"
IFS=$'\n'
for lingua in `cat $linguas`; do
  [[ "$lingua" =~ ^#.*$ ]] && continue
  echo "$lingua.po read from $linguas"
  msgmerge --update ./$lingua/LC_MESSAGES/$1.po ./templates/$1.pot
  echo "./$lingua/LC_MESSAGES/'$1'.po updated"
done

