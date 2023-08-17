from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(req):
    
    return render(req,'index.html')