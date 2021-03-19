
import csv
import sys
from argparse import ArgumentParser
from config.classes import Bairro, Arquivo, testes, formater

parser = ArgumentParser()
subparsers = parser.add_subparsers()

form = subparsers.add_parser('format')
form.add_argument('--arquivo_entrada', '-ae', type=str, help='Seleciona o arquivo de entrada', required=True)
form.add_argument('--arquivo_saida', '-as', type=str, help='Seleciona o arquivo de saída', required=True)
form.set_defaults(subparser='format')

calc = subparsers.add_parser('calc')
calc.add_argument('--municipio', '-m', action='store_true', help='Fazer conta do limiar por cada município')
calc.add_argument('--bairro', '-b', action='store_true', help='Fazer conta do limiar por cada Estacão/Bairro')
calc.add_argument('--format', '-f', action='store_true', help='Formata o arquivo de entrada')
calc.add_argument('--arquivo_entrada', '-ae', type=str, help='Seleciona o arquivo de entrada', required=True)
calc.add_argument('--arquivo_saida', '-as', type=str, help='Seleciona o arquivo de saída', required=True)
calc.add_argument('--limiarA', '-lA', type=str,help='Limiar A', required=True)
calc.add_argument('--limiarB', '-lB', type=str,help='Limiar A', required=True)
calc.set_defaults(subparser='calc')

args = parser.parse_args()

debug = False
if debug:
    entrada = 'resm_n.csv'
    la = 100
    lb = 300
    saida = 'resm_teste.csv'
else:
    if args.subparser == 'calc':
        entrada = args.arquivo_entrada
        la = args.limiarA
        lb = args.limiarB
        saida = args.arquivo_saida
        
    elif args.subparser == 'format':
        entrada = args.arquivo_entrada
        saida = args.arquivo_saida

if args.subparser == 'calc':
    Arq = Arquivo(entrada, saida)
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

elif args.subparser == 'format':
    form = formater(entrada, saida)
    form.forma()