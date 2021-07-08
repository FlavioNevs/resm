import sqlite3
import json 
import os

BASE_DIR = os.getcwd()
with open(f"{BASE_DIR}\\config.json", 'r', encoding='utf-8') as file:
    access = json.load(file)

class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

        self.__create_database()
        self.__create_table()
        self.__clear()
        self.__xcld('DatenumR', access['data']['xcld_date'])
        self.__xcld('Bairro', access['data']['xcld_bair'])

    def __connect(self):
        self.conn = sqlite3.connect(self.db_file)

    def __disconnect(self):
        self.conn.close()
        self.conn = None

    def __clear(self):
        self.__connect()
        cursor = self.conn.cursor()
        cursor.execute(f'UPDATE Dados SET ignore = 0')
        self.conn.commit()
        self.__disconnect()

    def __xcld(self, campo, datalist):
        self.__connect()
        cursor = self.conn.cursor()
        for row in datalist:
            cursor.execute(f"UPDATE Dados SET ignore = 1 WHERE {campo} = '{row}'")
        self.conn.commit()
        self.__disconnect()

    def exec_sql(self, sql):
        self.__connect()
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        self.__disconnect()

    def rain_lim_count(self, campo, lA, lB):
        self.__connect()
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT count(DatenumR) FROM Dados WHERE {campo} BETWEEN {lA} and {lB}")
        return cursor.fetchall()
    
    def rain_count(self, lA, lB):
        self.__connect()
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT count(DatenumR) FROM Dados WHERE max BETWEEN {lA} and {lB}")
        return cursor.fetchall()
    
    def event_lim_count(self, campo, local, event, lA, lB):
        if local is None:
            sql = f"SELECT count(DatenumR) FROM Dados WHERE Naturezadoevento = '{event}' AND {campo} BETWEEN {lA} AND {lB} and ignore != 1"
        else:
            sql = f"SELECT count(DatenumR) FROM Dados WHERE Naturezadoevento = '{event}' AND {campo} BETWEEN {lA} AND {lB} and ignore != 1 and Bairro = '{local}'"

        self.__connect()
        cursor = self.conn.cursor()
        cursor.execute(sql)
        if cursor.rowcount > 1:
            return [(0)]
        return cursor.fetchall()

    def mun_event_calc(self, lA, lB):
        self.__connect()
        cursor = self.conn.cursor()
        cursor.execute(f"select count(distinct(bairro)) from Dados where max between {lA} and {lB} and bairro is not null and ignore == 0 group by datenumR")
        if cursor.rowcount > 1:
            return [(0)]
        return cursor.fetchall()

    def __create_table(self):
        self.__connect()
        statement ="""CREATE TABLE IF NOT EXISTS `Dados` (
                        `ID` INTEGER AUTO_INCREMENT PRIMARY KEY,
                        `datenumR` INT, 
                        `Ano` INT,
                        `Mes` INT, 
                        `Dia` INT, 
                        `chuva` INT, 
                        `Bairro` TEXT, 
                        `chuva_acum` INT, 
                        `Naturezadoevento` TEXT, 
                        `max` REAL, `acumMunMax` REAL,`media` REAL, `min` REAL, `desvpad` REAL, 
                        `DAEE` REAL, `acumCENA` REAL, `acumDAEE` REAL, `CENA` REAL, 
                        `CENT` REAL, `acumCENT` REAL, `JDIN` REAL, `acumJDIN` REAL, 
                        `JDNL` REAL, `acumJDNL` REAL, `JDSC` REAL, `acumJDSC` REAL, 
                        `PQJA` REAL, `acumPQJA` REAL, `TABO` REAL, `acumTABO` REAL, 
                        `maxCENT` REAL, `acumMaxCENT` REAL, `maxCGDE` REAL, `acumMaxCGDE` REAL,
                        `ignore` BOOL
                        ); """
        cursor = self.conn.cursor()
        cursor.execute(statement)
        self.conn.commit()
        self.__disconnect()

    def __create_database(self):
        self.__connect()
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except:
            print('Erro durante a criação do Banco de Dados!')
        finally:
            if conn:
                conn.close()
                self.conn = None
