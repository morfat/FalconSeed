from utils.tables import Table

from utils.utils import current_date_time


class User(Table):
    pk="id"
    
    name="users"
    properties={
        "first_name": {
            "type": "string",
            "minLength":1,
            "maxLength":50
        },
        "last_name": {
            "type": "string",
        },
        "id":{
            "type":"string",
            "maxLength":100
        },
        "email": {
            "type": "string",
            "format":"email"
        },
        "password":{
            "type":"string",
            "writeOnly":True
        },
        "created_at": {
            "type": "string"
            #"format":   #"date-time" #there is also date
        },
    }
    required= ["email","password","id","created_at"]


    

   




            


    



   













    




