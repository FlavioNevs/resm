import csv

class formater:
    def __init__(self, entrada, saida):
        self.entrada = entrada
        self.saida = saida
    
    def forma(self):
        with open(self.entrada, "r", encoding="latin-1") as r:

            with open(self.saida, 'w') as outro:
                for row in r:
                    var = str(row)
                    var = var.replace(',', '.')
                    var = var.replace(';', ',')
                    var = var.replace('"', '')
                    outro.write(var)
class Arquivo:

    def __init__(self, nomeA, nomeB):
        self.nomeA = nomeA
        self.nomeB = nomeB

    def saver(self, la, lb, loc, nm):
        for local in loc:
            if nm == False:
                ver = f'_{local}.'
            else:
                ver = f'_{nm[loc.index(local)]}.'
            with open(self.nomeB.replace('.',ver ), 'a') as file:

                file.write(f'\n{la}_{lb}')

                for row in testes[local].items():
                    file.write(f',{str(row[1]["count"])}')

class Municipio:
    def __init__(self):
        self.dias = 0
        self.nats = {
            'munmax': [],
            'munmed': []
        }
        self.dict = {
            'Alagamento': 0,
            'Desabamento': 0,
            'Deslizamento': 0,
            'Escorregamento': 0,
            'Inundacao': 0,
            'Solapamento':  0,
            } 

    def dic_writer(self):
        for sel in self.dict.items():
            if sel[1] != 0:
                events[sel[0]][sel[1]] +=1

    def dic_reset(self):
        self.dict['Alagamento'] = 0
        self.dict['Desabamento'] = 0
        self.dict['Deslizamento'] = 0
        self.dict['Escorregamento'] = 0
        self.dict['Inundacao'] = 0
        self.dict['Solapamento'] = 0
    
    def dic_saver(self, la, lb):

        for env in events.items():
            with open(f'{env[0]}.csv', 'a') as file:
                file.write(f'\n{la}_{lb}')

                for rg in range(1, 6): 
                    file.write(f',{env[1][rg]}')
    
    def define(self, nat, dia, stat):
        ver = True
        if nat in self.nats[stat] and dia == self.dias:
            ver = False

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
        self.states = [12, 14 ,16, 18, 20, 22, 24, 26, 28, 29]
        self.names = ['DAEE', 'CENA', 'CENT', 'JDIN', 'JDNL', 'JDSC', 'PQJA', 'TABO', 'CENTRO', 'CGDE']
        self.dias = 0
        self.locais = []
        self.nats = []
        self.dicstat = False
        self.dict = {
            'geral': 0,
            'Alagamento': 0,
            'Desabamento': 0,
            'Deslizamento': 0,
            'Escorregamento': 0,
            'Inundacao': 0,
            'Solapamento':  0,
            } 

    def dic_writer(self):
        for sel in self.dict.items():
            if sel[1] != 0:
                events[sel[0]][sel[1]] +=1

    def dic_reset(self):
        self.dict['geral'] = 0
        self.dict['Alagamento'] = 0
        self.dict['Desabamento'] = 0
        self.dict['Deslizamento'] = 0
        self.dict['Escorregamento'] = 0
        self.dict['Inundacao'] = 0
        self.dict['Solapamento'] = 0
    
    def dic_saver(self, la, lb):

        for env in events.items():
            with open(f'{env[0]}.csv', 'a') as file:
                file.write(f'\n{la}_{lb}')

                for rg in range(1, 6): 
                    file.write(f',{env[1][rg]}')


    @staticmethod
    def finder(local):
        if local == "Conceicao":
            return [22]
        elif local == "Centro":
            return [14, 16, 24, 28]
        elif local == "Eldorado":
            return [18]
        elif local == "Casa Grande":
            return [12, 20, 29]
        elif local == "Taboao":
            return [14]
        else:
            return []

    def define(self, nat, local, dia,):
        ver = True

        for natur in self.nats:
            if nat == natur:
                for loc in self.locais:
                    if local == loc and dia == self.dias:
                        ver = False
                        break
        return ver

    @staticmethod
    def dine( nat, stat, local):
        nats = ['Alagamento', 'Desabamento', 'Deslizamento', 'Escorregamento', 'Inundacao', 'Solapamento']

        for nt in nats:
            ind = nats.index(nt) + 1
            if nat == nt:
                testes[stat][ind]['count'] += 1

                # se o local nao estiver na lista
                if local not in testes[stat][ind]['locais']:
                    testes[stat][ind]['locais'].append(local)


events = {
    'geral': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0},
    'Alagamento': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0},
    'Desabamento': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0},
    'Deslizamento': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0},
    'Escorregamento': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0},
    'Inundacao': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0},
    'Solapamento': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
}

testes = {
    12: {
        1: {'count': 0, 'locais': ['']},
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
    28: {
        1: {'count': 0, 'locais': ['']},
        2: {'count': 0, 'locais': ['']},
        3: {'count': 0, 'locais': ['']},
        4: {'count': 0, 'locais': ['']},
        5: {'count': 0, 'locais': ['']},
        6: {'count': 0, 'locais': ['']},
        'chu': {'count': 0, 'locais': ['']}
    },
    29: {
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