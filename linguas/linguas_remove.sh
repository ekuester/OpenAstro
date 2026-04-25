#!/bin/bash
# get filename as parameter $1 from command line e.g. openastro or astroChart
# start in directory 'linguas'
cd ../locale
linguas="../linguas/LINGUAS"
IFS=$'\n'
for lingua in `cat $linguas`; do
  [[ "$lingua" =~ ^#.*$ ]] && continue
  echo "$lingua.mo read from $linguas"
  rm -fv ./$lingua/LC_MESSAGES/$1.mo
  echo "./$lingua/LC_MESSAGES/'$1'.mo deleted"
done

