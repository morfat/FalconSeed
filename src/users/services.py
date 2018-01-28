from argon2 import PasswordHasher as ph

from .tables import User 

from utils.utils import current_date_time

from utils.services import BaseService

class UserService(BaseService):
    table_class=User
    ordering='created_at DESC'
    
    
    def insert(self,json_data):
        
        password=self.hash_password(json_data.get("password","12345"))
        json_data.update({"password":password,"created_at":self.get_unix_timestamp(),"id":self.get_uuid()})

        user=User()
        user.validate(json_data)
        json_data=user.get_cleaned_data()

      

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

        #remove write only keys from  being read
        json_data=user.get_display_data()


        self.db.execute(sql)
        self.db.commit()
        return json_data


    def hash_password(self,password):
        return ph().hash(password)

    def verify_password(self,hash,password):
        try:
            return ph().verify(hash,password)
        except:
            return False


