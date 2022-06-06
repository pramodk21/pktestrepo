import json

from flask import Blueprint
apiv2=Blueprint('apiv2',__name__,url_prefix='/apiv2')
@apiv2.route('/getdata')
def getdata():
   return "api Version 2 called"
