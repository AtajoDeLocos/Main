#!/bin/bash

logsbase="shopify.com"
#mkdir $logsbase/subdominios
while IFS="" read -r p;
do
    # Comandos
    #mkdir $logsbase/subdominios/$p
    nuclei -u $p > $logsbase/subdominios/$p/nuclei.txt
done < "$logsbase/subdominios.txt"
