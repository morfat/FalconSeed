from utils.database import MySQL

from falcon import HTTP_METHODS

class CORSMiddleWare:

    ALLOWED_ORIGINS=['*']


    def process_resource(self,req,resp,resource,params):
        origin=req.get_header('Origin')
        if origin:
            #if no origin then its not a valid CORS request
            acrm=req.get_header('Access-Control-Request-Method')
            acrh = req.get_header('Access-Control-Request-Headers')
            if req.method=='OPTIONS' and acrm and acrh:
                #this is preflight request

                # Set ACAH to echo ACRH
                resp.set_header('Access-Control-Allow-Headers', acrh)
                # Optionally set ACMA
                # resp.set_header('Access-Control-Max-Age', '60')

                # Find implemented methods
                allowed_methods = []
                for method in HTTP_METHODS:
                    allowed_method = getattr(resource, 'on_' + method.lower(), None)
                    if allowed_method:
                        allowed_methods.append(method)
                

                # Fill ACAM
                resp.set_header('Access-Control-Allow-Methods', ','.join(sorted(allowed_methods)))


    def process_response(self,req,resp,resource,req_succeeded): #called immediately before the response is returned.
        origin = req.get_header('Origin')
        if origin:
            # If there is no Origin header, then it is not a valid CORS request
            if '*' in self.ALLOWED_ORIGINS:
                resp.set_header('Access-Control-Allow-Origin', '*')
            elif origin in self.ALLOWED_ORIGINS:
                resp.set_header('Access-Control-Allow-Origin', origin)
        

class CoreMiddleWare:

    ALLOWED_ORIGINS=['*']

    def __init__(self,):
        self._db=None
       

    def process_request(self,req,resp):
        self._db=MySQL() #create db connection and Db object
    
    
    def process_resource(self,req,resp,resource,params):
        resource.db=self._db
        

    def process_response(self,req,resp,resource,req_succeeded): #called immediately before the response is returned.
        self._db.connection.close()


    


