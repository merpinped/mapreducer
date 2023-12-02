#!/usr/bin/python

import sys

oldSale = None

costoTotal = 0.0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    thisSale = float(line.strip())
    if thisSale == None:
        # Something has gone wrong. Skip this line.
        continue
	
    if (costoTotal < thisSale): costoTotal = thisSale

    oldSale = thisSale
    

# Escribe maximo absoluto de todas las ventas en caso de que el texto no viniese vacio.
if oldKey != None:
	print(f'El máximo absoluto de todas las ventas es {costoTotal}')
