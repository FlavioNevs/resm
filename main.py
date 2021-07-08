from models.model import DataBase
from ClassModule.termparser import get_args, verify
from ClassModule.utils import DB_PATH, access, writer, evc_writer

acum = True

def main():
    xp = {}
    data = get_args()
    db = DataBase(DB_PATH)

    if acum:
        val = "acumMunMax"
        stat_loc = access['data']['local_acum']
        stat_norm = access['data']['acum']
    else:
        val = "max"
        stat_loc = access['data']['local_norm']
        stat_norm = access['data']['norm']

    if data['bairro']:
        for loc in access['data']['local']:
            for stat in stat_loc[loc]:
                xp[stat] = {}
                xp[stat]['qt_chuva'] = db.rain_lim_count(stat, data['lA'], data['lB'])[0][0]
                for nat in access['data']['events']:
                    xp[stat][nat] = {}
                    xp[stat][nat] = int(db.event_lim_count(stat, loc, nat, data['lA'], data['lB'])[0][0])
        writer(data['outfile'], xp, stat_norm, data['lA'], data['lB'])

    elif data['municipio']:
        for nat in access['data']['events']:
            if val not in xp:
                xp[val] = {}
            
            xp[val]['qt_chuva'] = db.rain_lim_count(val, data['lA'], data['lB'])[0][0]
            xp[val][nat] = int(db.event_lim_count(val, None, nat, data['lA'], data['lB'])[0][0])

        xp['evc'] = {}
        for row in db.mun_event_calc(data['lA'], data['lB']):
            if row[0] not in xp['evc']:
                xp['evc'][row[0]] = 0
            xp['evc'][row[0]] += 1

        for x in range(1, 6):
            if x not in xp['evc']:
                xp['evc'][x] = 0

        writer(data['outfile'], xp, [val], data['lA'], data['lB'])
        evc_writer(data['outfile'], xp, ['evc'], data['lA'], data['lB'])


if __name__ == "__main__" and verify():
    main()