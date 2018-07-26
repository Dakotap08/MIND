import webapp2
import jinja2
import os
import  models

the_jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class homeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/landingPage.html')
        self.response.write(welcome_template.render())

app = webapp2.WSGIApplication([
    ('/', homeHandler)#this maps the root url to the EnterInfoHandler
     #this maps the root URL to the ShowMemeHandler
], debug=True)
