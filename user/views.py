from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def userRegister(request):
    form = KayitForm()
    if request.method == 'POST':
        form = KayitForm(request.POST)
        if form.is_valid():
            kayit = form.save(commit = False)
            subject = 'Neos Ticaret'
            message = 'Bu bir denemedir'
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [kayit.email],
                fail_silently=False,
            )
            kayit.save()
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'register.html', context) 

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['user']
        sifre = request.POST['sifre']
    
        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('index')
