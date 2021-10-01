#!/bin/bash
soma=0
diretorias=$*

if [ -z "$diretorias" ]; then
    while read linha
    do
        if [ -z "$linha" ]; then
            break
            # Não termina?
            # ./ex2-6.sh
            # /home
        fi
        diretorias+="$linha "
    done
fi

resfind=`find $diretorias -name "ficha*" -printf "%s "`
for i in $resfind
do
    let soma+=$i
done

echo "Soma: $soma"
