import webapp2
import uuid

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(str(uuid.uuid4()))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
])
