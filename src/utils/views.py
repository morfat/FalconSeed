import uuid

class BaseView(object):
    login_required=True
    user=None
    def reply(self,response,pagination=None,message=None):
        reply={}
        reply.update(response)

        if pagination and message:
            reply.update({'pagination':pagination,'message':message})
        elif pagination:
            reply.update({'pagination':pagination})
        elif message:
            reply.update({'message':message})
        return reply

    def unique_id(self):
        #return model uniue id
        return uuid.uuid4().hex
    