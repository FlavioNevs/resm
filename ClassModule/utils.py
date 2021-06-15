import os
import json

BASE_DIR = os.getcwd()
with open(f"{BASE_DIR}\\config.json", 'r', encoding='utf-8') as file:
    access = json.load(file)


def json_dump(data):
    with open(f"{BASE_DIR}\\result.json", 'w', encoding='utf-8') as file:
        json.dump(data, file)


def writer(filename, data, stat, lA, lB):
    for stat in stat:
        with open(filename.replace('.csv', f"_{stat}.csv"), 'a', encoding='utf-8') as file:
            file.write(f"{lA}_{lB},{data[stat][access['data']['events'][0]]},{data[stat][access['data']['events'][1]]},{data[stat][access['data']['events'][2]]},{data[stat][access['data']['events'][3]]},{data[stat][access['data']['events'][4]]},{data[stat]['qt_chuva']}\n")

def evc_writer(filename, data, stat, lA, lB):
    for stat in stat:
        with open(filename.replace('.csv', f"_{stat}.csv"), 'a', encoding='utf-8') as file:
            file.write(f"{lA}_{lB},{data[stat][1]},{data[stat][2]},{data[stat][3]},{data[stat][4]},{data[stat][5]}\n")


DB_PATH = f"{BASE_DIR}{access['local']['db']}"