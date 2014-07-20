import cherrypy


class PurchasingManagementMonitoring(object):
    @cherrypy.expose
    def index(self):
        return "Here be dragons"
