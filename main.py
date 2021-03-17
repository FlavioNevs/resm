import sys
import csv
from set import saver, testes, finder, define

# abre o arquivo da lista
with open(sys.argv[1], "r") as ff:
    resm = csv.reader(ff)

    states = [7, 8, 9, 10, 11, 12, 13, 14]
    names = ['DAEE', 'CENA', 'CENT', 'JDIN', 'JDNL', 'JDSC', 'PQJA', 'TABO']
    dias = []
    ctd = []
    locais = []
    nats = []

    # Analisa liha por linha do código
    for row in resm:
        # Analiza por estação
        for stat in states:

            # NA é a mesma coisa que 0, mas né...
            if row[stat] == 'NA':
                resender = False
            else:
                # Verificação do Limiar
                limiar = float(row[stat])
                if limiar > int(sys.argv[2]) and limiar <= int(sys.argv[3]):
                    if not row[0] in ctd:
                        testes[stat]['chu']['count'] += 1
                        ctd.append(row[0])
                    resender = True
                else:
                    resender = False
            # Verificação da estação condizente

            for result in finder(row[6]):
                if resender and result == stat:
                    # Salva os dados
                    define(row[5], stat, row[6], row[0], dias, locais, nats)
        states = [7, 8, 9, 10, 11, 12, 13, 14]


    # Pergunta o nome que o arquivo vai ser salvo e salva <set.saver()>
    name = sys.argv[4]
    saver(name, states, names)