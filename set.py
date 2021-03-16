# Verificador do local
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


def define(nat, stat, local, dia, dias, locais, nats):
    ct = 0
    ver = True

    for dd in dias:
        if dd == dia:
            if locais[ct] == local and nats[ct] == nat:
                ver = False
                break
            else:
                ct += 1
        else:
            ct += 1
    if ver:
        dine(nat, stat, local)
        dias.append(dia)
        locais.append(local)
        nats.append(nat)


def dine(nat, stat, local):
    nats = ['Alagamento', 'Desabamento', 'Deslizamento', 'Escorregamento', 'Inundacao', 'Solapamento']

    for nt in nats:
        ind = nats.index(nt) + 1
        if nat == nt:
            testes[stat][ind]['count'] += 1
            if local not in testes[stat][ind]['locais']:
                testes[stat][ind]['locais'].append(local)

def saver(name, states, names):
    with open(name, 'w') as file:
        file.write('ID,Alagamento,Desabamento,Deslizamento,Escorregamento,Inundacao,Solapamento,QtChuva')

        for rw in states:
            file.write('\n' + names[states.index(rw)])

            for row in testes[rw].items():
                file.write(',' + str(row[1]['count']))

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
}