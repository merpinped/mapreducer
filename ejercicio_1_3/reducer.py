#!/usr/bin/python

import sys

oldKey = None

ventasMasAltas = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    # Escribe un par key:value no dicc ante un cambio na key
    if thisKey in ventasMasAltas:
	if(ventasMasAltas[thisKey] < thisSale): ventasMasAltas[thisKey] = thisSale
    else:
        ventasMasAltas[thisKey] = thisSale

    # Comprueba si la venta guardada en el diccionario es menor que la nueva venta en esta linea.
    oldKey = thisKey
    

# Escribe o diccionario cas ventas mais altas para cada metodo de pago
if oldKey != None:
    for m, v in ventasMasAltas.items():
	print(m+"\t"+v)
