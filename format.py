import csv
import sys

with open(sys.argv[1], "r", encoding="latin-1") as r:
    resm = csv.reader(r)

    with open(sys.argv[2], 'w') as outro:
        for row in resm:
            var = str(row[0])
            var = var.replace(';', ',')
            var = var.replace('"', '')
            outro.write(var+'\n')