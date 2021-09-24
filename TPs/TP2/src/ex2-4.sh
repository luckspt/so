#!/bin/bash
positivos=0
negativos=0
zeros=0
if [ $1 ]; then
    for i in $*
    do
        if [ $i -lt 0 ]; then
            let negativos=$negativos+1
        elif [ $i -eq 0 ]; then
            let zeros=$zeros+1
        else let positivos=$positivos+1
        fi
    done
    
    echo "Negativos: $negativos"
    echo "Zeros: $zeros"
    echo "Positivos: $positivos"

else
    echo "Erro: falta um argumento"
fi