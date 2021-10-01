#!/bin/bash
soma=0
resfind=`find . -name "ficha*" -printf "%s "`
for i in $resfind
do
    let soma+=$i
done

echo "Soma: $soma"
