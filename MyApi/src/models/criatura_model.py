from database.db import get_connection
from .entitys.criatura import Criatura

class CriaturaModel():
    
    @classmethod
    def get_criaturas(self):
        try:
            connection = get_connection()
            criaturas = []
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM public."EldenDexApp_creatures" ORDER BY id ASC')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    criatura=Criatura(row[0], row[1], row[2], row[3], row[4], row[5])
                    criaturas.append(criatura.to_json())
            
            connection.close()
            return criaturas
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def getByName(self, name):
        try:
            connection = get_connection()
            criaturas = []
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM public."EldenDexApp_creatures" WHERE name LIKE ' + "'{}%'".format(name))
                resultset = cursor.fetchall()
                if resultset != None:
                    for row in resultset:
                        criatura=Criatura(row[0], row[1], row[2], row[3], row[4], row[5])
                        criaturas.append(criatura.to_json())
            
            connection.close()
            return criaturas
            
        except Exception as ex:
            raise Exception(ex)