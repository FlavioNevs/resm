from model import DataBase

db = DataBase('models\\DataResm.db')
with open('models\\DataVanessa3.sql', 'r') as file:
    for row in file:
        print(row)
        db.exec_sql(row)
    