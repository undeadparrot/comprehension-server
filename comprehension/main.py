import json
import falcon

class Login:
    def on_get(self, request, response):
        response.body = json.dumps({"status": "OK"})

class OAuth:
    def on_get(self, request, response):
        breakpoint()
    def on_post(self, request, response):
        breakpoint()

application = falcon.API()
application.add_route('/login', Login())
application.add_route('/oauth', OAuth())

