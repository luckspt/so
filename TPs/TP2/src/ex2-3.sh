#!/bin/bash
if [ $1 ]; then
    for i in $*
    do
        if [ $i -lt 0 ]; then
            echo "$i e’ um numero inteiro negativo"
        elif [ $i -eq 0 ]; then
            echo "$i e’ o numero zero"
        else echo "$i e’ um numero inteiro positivo"
        fi
    done

else echo "Erro: falta um argumento"
fi