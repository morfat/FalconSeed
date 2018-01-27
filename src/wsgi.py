
#This contains the deployable content for the whole project

import falcon

#General

from utils.middlewares import CoreMiddleWare,CORSMiddleWare

#from utils.handlers import api_error_handler

#custom apps

from users.urls import patterns as users_patterns


URL_PATTERNS=[users_patterns]



def get_app():
    app=falcon.API(middleware=[CORSMiddleWare(),CoreMiddleWare(),],)
   
    #add routes 

    for up in URL_PATTERNS:
        for i in up:
             app.add_route(i[0],i[1])
            

    #add cutom error handler
    #app.add_error_handler(falcon.HTTPError,handler=api_error_handler)
    
    return app


application=get_app()