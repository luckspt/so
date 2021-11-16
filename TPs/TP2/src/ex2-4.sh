#!/bin/bash
positivos=0
negativos=0
zeros=0
if [ $# -gt 0 ]; then
    for i in $*
    do
        if [ $i -lt 0 ]; then
            let negativos++
        elif [ $i -eq 0 ]; then
            let zeros++
        else let positivos++
        fi
    done
    
    echo "Negativos: $negativos"
    echo "Zeros: $zeros"
    echo "Positivos: $positivos"

else
    echo "Erro: falta um argumento"
fi