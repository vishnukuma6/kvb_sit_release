from django.contrib.sites import requests
import requests

from Bigflow.Core import views as Core_Views
## Role Based Token Will Assign if needed
def token(request):
    acces_token = Core_Views.token_jwt(request,"CHECK",'')
    return "Bearer  " + acces_token