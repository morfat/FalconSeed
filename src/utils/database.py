import MySQLdb


from src.settings import DATABASE




class MySQL:
    def __init__(self,):
        self.connection=MySQLdb.connect(user=DATABASE.get('USER'),passwd=DATABASE.get('PASSWORD'),
                                db=DATABASE.get('NAME'),host=DATABASE.get('HOST'),port=DATABASE.get('PORT')
                            )
        self.cursor=None

      
    def execute(self,sql):
        self.cursor=self.connection.cursor()
        self.cursor.execute(sql)
        return self

    def commit(self,commit=True):
        if commit:
            self.connection.commit()
            

    def fetchall(self,as_dict=False):
        if as_dict:
            results=[dict(zip([col[0] for col in self.cursor.description], row)) for row in self.cursor.fetchall()]
        else:
            results=self.cursor.fetchall()
        self.cursor.close()
        return results

    def fetchone(self):
        "Return one row from a cursor as a dict"
        if self.cursor.rowcount==0:
            result=None
        else:
            result=dict(zip([col[0] for col in self.cursor.description], self.cursor.fetchone()))
        self.cursor.close()
        return result

        



    




        

         

          