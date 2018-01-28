import falcon


from falcon.media.validators import jsonschema
from users.services import UserService
from utils.views import BaseView


class ListCreateView(BaseView):
    

    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default

        userService=UserService(self.db)

        users=userService.get_users()

        resp.media=self.reply({"users":users},pagination={},message="Well Done")



    def on_post(self,req,resp):
        userService=UserService(self.db)

        user={"email":"me@me913.com","password":"pass","first_name":"Mosoti","last_name":"mogaka","id":self.unique_id()}

        inserted=userService.insert(user)

        #data=req.media
        resp.media=self.reply({"user":inserted})


