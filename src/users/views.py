import falcon


from falcon.media.validators import jsonschema
from users.services import UserService


class ListCreateView(object):

    userService=UserService()
    

    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default
        
        users=self.userService.get_users()

        resp.media={"users":users}


    def on_post(self,req,resp):
        resp.status=falcon.HTTP_201 #this is default

        data=req.media
        user={}

        resp.media=user


