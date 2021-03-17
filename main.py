
import csv
import sys
from config.classes import Modulo, Arquivo, testes

debug = True
if debug:
    arquivo_entrada = 'resm.csv'
    la = 100
    lb = 300
    arquivo_saida = 'resm_teste.csv'
else:
    arquivo = sys.argv[1]
    la = int(sys.argv[2])
    lb = int(sys.argv[3])
    name = sys.argv[4]

Arq = Arquivo(arquivo_entrada, arquivo_saida)
with open(Arq.nomeA, 'r') as f:
    file = csv.reader(f)
    mod = Modulo()

    for row in file:
        if row[0] != mod.dias:
            mod.locais = []
            mod.nats = []

        for stat in mod.states:
            if row[stat] == 'NA':
                resender = False
            elif la < float(row[stat]) <= lb:
                if row[0] != mod.dias:
                    testes[stat]['chu']['count'] += 1
                    testes[15]['chu']['count'] += 1
                resender = True
            else:
                resender = False

            for result in mod.finder(row[6]):
                ver = False
                if resender and result == stat:
                    ver = mod.define(row[5], stat, row[6], row[0])
                elif resender:
                    ver = mod.define(row[5], stat, row[6], row[0])

                if ver:
                    mod.dine(row[5], stat, row[6])
                    mod.dine(row[5], 15, row[6])
                    mod.locais.append(row[6])
                    mod.nats.append(row[5])

        mod.dias = row[0]


        mod.states = [7, 8, 9, 10, 11, 12, 13, 14]
    Arq.saver(mod.states, mod.names)