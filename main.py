
import csv
import sys
from argparse import ArgumentParser
from config.classes import Bairro, Arquivo, testes, formater, Municipio

parser = ArgumentParser()
subparsers = parser.add_subparsers()

form = subparsers.add_parser('format')
form.add_argument('--arquivo_entrada', '-ae', type=str, help='Seleciona o arquivo de entrada', required=True)
form.add_argument('--arquivo_saida', '-as', type=str, help='Seleciona o arquivo de saída', required=True)
form.set_defaults(subparser='format')

calc = subparsers.add_parser('calc')
calc.add_argument('--municipio', '-m', action='store_true', help='Fazer conta do limiar por cada município')
calc.add_argument('--bairro', '-b', action='store_true', help='Fazer conta do limiar por cada Estacão/Bairro')
calc.add_argument('--arquivo_entrada', '-ae', type=str, help='Seleciona o arquivo de entrada', required=True)
calc.add_argument('--arquivo_saida', '-as', type=str, help='Seleciona o arquivo de saída', required=True)
calc.add_argument('--limiarA', '-lA', type=int,help='Limiar A', required=True)
calc.add_argument('--limiarB', '-lB', type=int,help='Limiar A', required=True)
calc.set_defaults(subparser='calc')

args = parser.parse_args()

if args.subparser == 'calc':
    entrada = args.arquivo_entrada
    la = args.limiarA
    lb = args.limiarB
    saida = args.arquivo_saida
    mun = args.municipio
    bai = args.bairro
    
elif args.subparser == 'format':
    entrada = args.arquivo_entrada
    saida = args.arquivo_saida

if args.subparser == 'calc' or debug:
    Arq = Arquivo(entrada, saida)
    if bai:
        with open(Arq.nomeA, 'r') as f:
            file = csv.reader(f)
            mod = Bairro()

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
                        resender = True
                    else:
                        resender = False

                    for result in mod.finder(row[7]):
                        ver = False
                        if resender and result == stat:
                            ver = mod.define(row[6], row[7], row[0])
                        elif resender:
                            ver = mod.define(row[6], row[7], row[0])

                        if ver:
                            mod.dine(row[6], stat, row[7])
                            mod.locais.append(row[7])
                            mod.nats.append(row[6])

                mod.dias = row[0]
                mod.states = [12, 14, 16, 18, 20, 22, 24, 26]
            Arq.saverB(mod.states, mod.names)
    elif mun:
        with open(Arq.nomeA, 'r') as f:
            file = csv.reader(f)
            mod = Municipio()

            st = ['munmed', 'munmax']
            for row in file:
                for stat in st:
                    resender = False
                    if row[0] != mod.dias:
                        mod.nats = []

                    if stat == 'munmed':
                        limiar = row[8]
                    elif stat == 'munmax':
                        limiar = row[10]

                    if la < float(limiar) <= lb:
                        #print(f'{row[0]} | {la} > {limiar} <= {lb}')
                        if row[0] != mod.dias:
                            testes[stat]['chu']['count'] += 1
                        resender = True
                    else:
                        resender = False
                    
                    if resender:
                        if row[6] != '':
                            ver = mod.define(row[6], row[0])

                            if ver:
                                mod.dine(row[6], stat)
                                print(f'{row[0]} - {row[6]}')
                                mod.nats.append(row[6])

                    mod.dias = row[0]

                
            for stat in st:
                Arq.saverM(la, lb, stat)
            

elif args.subparser == 'format':
    form = formater(entrada, saida)
    form.forma()