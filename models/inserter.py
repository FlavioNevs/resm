from model import DataBase

db = DataBase('DataResm.db')
with open('DataVanessa.sql', 'r') as file:
    for row in file:
        db.exec_sql(row)
        print(row)