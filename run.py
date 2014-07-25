import cherrypy
from app.main import PurchasingManagementMonitoring

cherrypy.quickstart(PurchasingManagementMonitoring())
