import os, os.path
import random
import string
import subprocess

import cherrypy


class HyperionServer(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')


@cherrypy.expose
class HyperionServiceManagementWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
    	#TODO return if service is executing
    	result = "yes"
        return result

    def POST(self, status="0"):
    	result = ""
    	if (status == "0"):
       		print "Turn to the other status"
       	if (status == "on"):
    		print "Execute webService"
    	if (status == "off" ):
    		print "shutdown webService"
    	result = "ok"
        return result


@cherrypy.expose
class HyperionPriorityClearer(object):

    @cherrypy.tools.accept(media='text/plain')    
    def POST(self):
        result='ok'
        subprocess.check_call(['/scripts/clear-priority.sh'])
        return result

@cherrypy.expose
class HyperionColorChanger(object):

    @cherrypy.tools.accept(media='text/plain')    
    def POST(self, color):
        result='ok'
        colorString = str(color);
        subprocess.check_call(['/scripts/color-change.sh', colorString])
        return result

@cherrypy.expose
class HyperionLuminanceChanger(object):

    @cherrypy.tools.accept(media='text/plain')    
    def POST(self, luminance):
        result='ok'
        luminanceString = str(luminance);
        subprocess.check_call(['/scripts/luminance-change.sh', luminanceString])
        return result


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },        
        '/hyperionService': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/clearPriority': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/changeColor': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/changeLuminance': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    webapp = HyperionServer()
    webapp.hyperionService = HyperionServiceManagementWebService()
    webapp.clearPriority = HyperionPriorityClearer()
    webapp.changeColor = HyperionColorChanger()
    webapp.changeLuminance = HyperionLuminanceChanger()
    cherrypy.quickstart(webapp, '/', conf)