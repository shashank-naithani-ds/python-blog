'''
HttpResponse only show text type values not the htmlpages
Render will render pages with values

from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return HttpResponse("This is homepage")
    or
    return render(req, 'home.html')
'''



    
    