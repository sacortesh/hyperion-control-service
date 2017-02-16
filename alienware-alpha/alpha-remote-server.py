import os, os.path
import random
import string
import subprocess
import cherrypy

class AlienwareControlMain(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

@cherrypy.expose
class AlienwareControlHDMIWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
    	#TODO return if service is executing
    	result = "yes"
        return result

    def POST(self):
    	result = ""
    	
        #subprocess.call("hdmi-switch-script.vbs")

    	result = "ok"
        return result


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/hdmiSwitch': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    webapp = AlienwareControlMain()    
    webapp.hdmiSwitch = AlienwareControlHDMIWebService()
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 9090
    cherrypy.quickstart(webapp, '/', conf)