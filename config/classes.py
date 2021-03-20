import csv

class formater:
    def __init__(self, entrada, saida):
        self.entrada = entrada
        self.saida = saida
    
    def forma(self):
        with open(self.entrada, "r", encoding="latin-1") as r:
            resm = csv.reader(r)

            with open(self.saida, 'w') as outro:
                for row in resm:
                    var = str(row[0])
                    var = var.replace(';', ',')
                    var = var.replace('"', '')
                    outro.write(var+'\n')
class Arquivo:

    def __init__(self, nomeA, nomeB):
        self.nomeA = nomeA
        self.nomeB = nomeB
        self.titulo = 'ID,Alagamento,Desabamento,Deslizamento,Escorregamento,Inundacao,Solapamento,QtChuva'

    def saverB(self, states, names):
        with open(self.nomeB, 'w') as file:
            file.write(self.titulo)

            for rw in states:
                file.write('\n' + names[states.index(rw)])

                for row in testes[rw].items():
                    file.write(',' + str(row[1]['count']))

    def saverM(self, la, lb, loc):
        if loc == 'munmed':
            ver = '_med.'
        else:
            ver = '_max.'

        with open(self.nomeB.replace('.', ver), 'a') as file:

            file.write(f'\n{la}_{lb}')

            for row in testes[loc].items():
                file.write(',' + str(row[1]['count']))

class Municipio:
    def __init__(self):
        self.dias = 0
        self.nats = []
    
    def define(self, nat, dia,):
        ver = True
        for natur in self.nats:
            if nat == natur and dia == self.dias:
                ver = False
                break
        return ver
    
    @staticmethod
    def dine(nat, loc):
        nats = ['Alagamento', 'Desabamento', 'Deslizamento', 'Escorregamento', 'Inundacao', 'Solapamento']

        for nt in nats:
            ind = nats.index(nt) + 1
            if nat == nt:
                testes[loc][ind]['count'] += 1

class Bairro:
    def __init__(self):
        self.states = [12, 14 ,16, 18, 20, 22, 24, 26]
        self.names = ['DAEE', 'CENA', 'CENT', 'JDIN', 'JDNL', 'JDSC', 'PQJA', 'TABO']
        self.dias = 0
        self.locais = []
        self.nats = []

    @staticmethod
    def finder(local):
        if local == "Conceicao":
            return [12]
        elif local == "Centro":
            return [8, 9, 13]
        elif local == "Eldorado":
            return [10]
        elif local == "Casa Grande":
            return [7, 11]
        elif local == "Taboao":
            return [14]
        else:
            return []

    def define(self, nat, local, dia,):
        ct = 0
        ver = True

        for natur in self.nats:
            if nat == natur:
                for loc in self.locais:
                    if local == loc and dia == self.dias:
                        ver = False
                        break
        return ver

    @staticmethod
    def dine(nat, stat, local):
        nats = ['Alagamento', 'Desabamento', 'Deslizamento', 'Escorregamento', 'Inundacao', 'Solapamento']

        for nt in nats:
            ind = nats.index(nt) + 1
            if nat == nt:
                testes[stat][ind]['count'] += 1

                # se o local nao estiver na lista
                if local not in testes[stat][ind]['locais']:
                    testes[stat][ind]['locais'].append(local)


testes = {
    12: {
        1: {
            'count': 0, 
            'locais': ['']
        },
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    14: {1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
        },
    16: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    18: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    20: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    22: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    24: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    26: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    'munmed': {
        1: {'count': 0},
        2: {'count': 0},
        3: {'count': 0},
        4: {'count': 0},
        5: {'count': 0},
        6: {'count': 0},
        'chu': {'count': 0}
    },
    'munmax': {
        1: {'count': 0},
        2: {'count': 0},
        3: {'count': 0},
        4: {'count': 0},
        5: {'count': 0},
        6: {'count': 0},
        'chu': {'count': 0}
    }
}