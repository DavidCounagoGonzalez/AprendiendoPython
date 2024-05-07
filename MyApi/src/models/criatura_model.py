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
        
    @classmethod
    def getById(self, id):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM public."EldenDexApp_creatures" WHERE id = %s',(id,))
                row = cursor.fetchone()
                criatura = None
                if row != None:
                    criatura=Criatura(row[0], row[1], row[2], row[3], row[4], row[5])
                    criatura = criatura.to_json()
                    
            connection.close()
            return criatura
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def addCriatura(self, criatura):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public."EldenDexApp_creatures"
                               (id, name, image, description, location, drops)
	                                VALUES (%s, %s, %s, %s, %s, %s)""", (criatura.id, criatura.name, criatura.image, criatura.description, 
                                                                        criatura.location, criatura.drops))
                
                affected_rows = cursor.rowcount
                connection.commit()        
            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def deleteCriatura(self, criatura):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM public."EldenDexApp_creatures" WHERE id =' + "'{}'".format(criatura.id))
                
                affected_rows = cursor.rowcount
                connection.commit()        
            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def updateCriatura(self, criatura):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public."EldenDexApp_creatures" SET name='{0}', image='{1}', description='{2}', location='{3}', drops= ARRAY{4}
                                    WHERE id = """.format(criatura.name, criatura.image, criatura.description, criatura.location, criatura.drops) + 
                                                "'{}'".format(criatura.id))
                
                affected_rows = cursor.rowcount
                connection.commit()        
            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise Exception(ex)