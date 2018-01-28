import falcon


from falcon.media.validators import jsonschema
from users.services import UserService
from utils.views import BaseView


class ListCreateView(BaseView):
    

    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200 #this is default

        userService=UserService(db=self.db,url=req.uri,query_params=req.params)

        users,pagination=userService.all(pagination=True)

        resp.media=self.reply({"users":users},pagination=pagination,message="Well Done")



    def on_post(self,req,resp):
        userService=UserService(self.db)
        inserted=userService.insert(req.media)
        resp.media=self.reply({"user":inserted})


