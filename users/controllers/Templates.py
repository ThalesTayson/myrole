from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from users.forms.Auth import formAuthenticate

def entrar(req):
    
    form = formAuthenticate()
    
    if ( req.POST ):
        form = formAuthenticate(req.POST, req.FILES)
        if form.is_valid():
            user = form.login()
            login(req, user)
            return redirect('home')

    return render(req,'login.html', {"form":form})

@login_required
def sair(req):
    logout(req)
    return redirect('home')