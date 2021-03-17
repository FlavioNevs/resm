import csv
import sys

rr = open(sys.argv[1], "r")
resm = csv.reader(rr)

with open(sys.argv[2], 'w') as outro:
    for row in resm:
        for itens in row:
            var = itens.replace(';', ',')
            var = itens.replace('"', '')
            outro.write(var+'\n')