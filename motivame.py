#!/usr/bin/env python3

#Esta es una pequena aplicacion para ayudarme a motivar mi trabajo

import math
import sys

total = int(sys.argv[1])
new_total = total
i = 1
last_groups = total

def print_bar(x, total):
    for j in range(1, 10):
        if j <= round( (x * 10) / total ):
            print('*', end = '')
        else:
            print('-', end = '')
    return True

for x in range(1, total + 1):
    left = new_total - (i - 1)
    groups = round(left / i)
    gsize = i
    
    #Busca resetear el contador si hay repeticiones
    if groups == last_groups:
        new_total = left
        i = 1
        groups = round(left / i)
        gsize = i
    
    
    
    print(str(x) + " - Restantes: " + str(left) + " - Te faltarian " + str(groups) + " grupo(s) de " + str(gsize) + "- Progreso = <", end = '')
    print_bar(x, total)
    print(">")
    last_groups = groups
    i += 1
