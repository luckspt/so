#!/bin/bash
diretorias=0
ficheiros=0

# 1. Usar resultado de comandos:
# let diretorias=`ls -l | grep "^d" -c`
# let ficheiros=`ls -l | grep "^-" | wc -l`

# 2. Incrementar dependendo de "-" ou "d"
# Guardar o output de ls -l num ficheiro
ls -l > lsout
while read linha
do
    if [ "${linha:0:1}" = "d" ]; then
        let diretorias++
    elif [ "${linha:0:1}" = "-" ]; then
        let ficheiros++
    fi
# Alimentar o while com o ficheiro
done < lsout
# Remover o ficheiro
rm lsout

echo "Diretorias: $diretorias"
echo "Ficheiros: $ficheiros"