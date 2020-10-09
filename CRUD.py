'''
import falcon
class Resource(object):
    def on_get(self, req, resp):
        #Handles Get requests
        resp.status = falcon.HTTP_200
        resp.body = ('I am doing my Sample API using Falcon.\n TAUSIF JUNAID')
app = falcon.API()
things = Resource()
app.add_route('/things',things)
'''

import falcon
class CRUD(object):
    def on_get(self,req,resp):
        resp.status = falcon.HTTP_200
        resp.body = "Falcon GET Method"
    def on_post(self,req,resp):
        resp.status = falcon.HTTP_201
        resp.body = "Falcon POST Method"
    def on_put(self,req,resp):
        resp.status = falcon.HTTP_202
        resp.body = "Falcon PUT Method"
    def on_delete(self,req,resp):
        resp.status = falcon.HTTP_204
        resp.body = "Falcon Delete Method"
    
api=falcon.API()
api.add_route('/',CRUD())
