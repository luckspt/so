#!/bin/bash
if [ $# -gt 0 ]; then
    soma=0
    for i in $*
    do
        let soma+=$i
    done
    
    echo "Soma: $soma"

else
    echo "Erro: falta um argumento"
fi