from argon2 import PasswordHasher as ph
import uuid

from .tables import User 

from utils.utils import current_date_time,unix_timestamp

from utils.pagination import get_paginated_response

from src.settings import PAGINATION

class UserService:
    def __init__(self,db,url,query_params):
        self.db=db
        self.url=url
        self.query_params=query_params
        self.table=User()



    def get_users(self,pagination=None):
        user=User()
        fields=','.join(user.get_display_fields())
        sql="SELECT %s FROM users ORDER BY created_at DESC "%(fields)

        if pagination:
            sql,pagination=self.paginate(sql)

        self.db.execute(sql)

        return (self.db.fetchall(),pagination,)


    def count(self,sql=None):
        if not sql:
            self.db.execute("SELECT count(*) as total_count FROM %s "%(self.table.name))
        else:
            sql_count='SELECT count(*) as total_count '+sql[sql.find('FROM'):]
            self.db.execute(sql_count)

        result=self.db.fetchone()
        return result.get('total_count')


    def paginate(self,sql):
        page=int(self.query_params.get('page',1))

        page_size=int(self.query_params.get('page_size',PAGINATION.get('page_size')))

        offset=(page-1)*page_size
        limit=page_size

        count=self.count(sql=sql)
        
        #real query
        sql=sql+' LIMIT %s , %s '%(offset,limit)
        pagination=get_paginated_response(self.url,page_size,page,offset,limit,count)
        return (sql,pagination,)


    
    def insert(self,json_data):
        
        password=self.hash_password(json_data.get("password","12345"))
        json_data.update({"password":password,"created_at":unix_timestamp(),"id":uuid.uuid4().hex})

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


