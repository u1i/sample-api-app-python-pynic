from pycnic.core import WSGI, Handler

class Hello(Handler):
    def get(self, name="World"):
        return { "message":"Hello, %s!"%(name) }
    def post(self, name="World"):
        return { "message":"Hello, %s!"%(name) }

class app(WSGI):
    routes = [
        ('/', Hello()),
        ('/([\w]+)', Hello())
    ]
