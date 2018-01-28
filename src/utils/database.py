import MySQLdb


from src.settings import DATABASE


class MySQL:
    def __init__(self,):
        self.connection=MySQLdb.connect(user=DATABASE.get('USER'),passwd=DATABASE.get('PASSWORD'),
                                db=DATABASE.get('NAME'),host=DATABASE.get('HOST'),port=DATABASE.get('PORT')
                            )
        self.cursor=None

      
    def execute(self,sql):
        self.cursor=self.connection.cursor(MySQLdb.cursors.DictCursor)
        self.cursor.execute(sql)
        return self

    def commit(self,commit=True):
        if commit:
            self.connection.commit()
            

    def fetchall(self):
        results=self.cursor.fetchall()
        self.cursor.close()
        return results

    def fetchone(self):
        result=self.cursor.fetchone()
        self.cursor.close()
        return result
    



        



    




        

         

          