#!/bin/bash
if [ $1 ]; then
    soma=0
    for i in $*
    do
        let soma=$soma+$i
    done
    
    echo "Soma: $soma"

else
    echo "Erro: falta um argumento"
fi