import json
import falcon

class Login:
    def on_get(self, request, response):
        response.body = json.dumps({"status": "OK"})

application = falcon.API()
application.add_route('/login', Login())

