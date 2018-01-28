
class UserService:
    def __init__(self,db):
        self.db=db


    def get_users(self):
        self.db.execute("SELECT * FROM users ")
        return self.db.fetchall()

    def insert(self,json_data):

        keys=[]
        values=[]

        for k,v in json_data.items():
            keys.append(k)

            if type(v) is str:
                v=' "%s" '%(v)

            values.append(v)

        keys=','.join(keys)
        values=','.join(values)

        sql="INSERT INTO users (%s) VALUES (%s) "%(keys,values)
        print (sql)

        self.db.execute(sql)
        self.db.commit()
        return json_data


