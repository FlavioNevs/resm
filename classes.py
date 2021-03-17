
class Arquivo:

    def __init__(self, nomeA, nomeB):
        self.nomeA = nomeA
        self.nomeB = nomeB
        self.titulo = 'ID,Alagamento,Desabamento,Deslizamento,Escorregamento,Inundacao,Solapamento,QtChuva'

    def saver(self, states, names):
        file = open(self.nomeB, 'w')
        file.write(self.titulo)

        for rw in states:
            file.write('\n' + names[states.index(rw)])

            for row in testes[rw].items():
                file.write(',' + str(row[1]['count']))

        file.write(('\n' + 'Total'))
        for row in testes[15].items():
            file.write(',' + str(row[1]['count']))


class Modulo:

    def __init__(self):
        self.states = [7, 8, 9, 10, 11, 12, 13, 14]
        self.names = ['DAEE', 'CENA', 'CENT', 'JDIN', 'JDNL', 'JDSC', 'PQJA', 'TABO']
        self.dias = 0
        self.locais = []
        self.nats = []
        self.loc = {
            'Conceicao': [12],
            'Centro': [8, 9, 13],
            'Eldorado': [10],
            'Casa Grande': [7, 11],
            'Taboao': [14]
        }

    def counterplus(self, dia, local, nat):
        self.dias.append(dia)
        self.locais.append(local)
        self.nats.append(nat)

    @staticmethod
    def finder(local):
        """
        for item in self.loc.items():
            for it in item:
                print(it)
                if local == item[0]:
                    return item[1]
                else:
                    return []
        """
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

    def define(self, nat, stat, local, dia,):
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
                if local not in testes[stat][ind]['locais']:
                    testes[stat][ind]['locais'].append(local)


testes = {
    7: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    8: {1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
        },
    9: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    10: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    11: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    12: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    13: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    14: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    15: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    }
}