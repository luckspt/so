#!/bin/bash
soma=0
while read linha
do
    if [ -z "$linha" ]; then
        break
    fi
    let soma+=$linha
done

echo "Soma: $soma"