from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    search = ''
    kategoriler = Kategori.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    context = {
        'urun':urunler,
        'kategoriler':kategoriler,
        'search':search
    }
    return render(request, 'index.html', context)

def olustur(request):
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'olustur.html', context)

def detail(request, id):
    urun = Urun.objects.filter(id = id)
    context = {
        'urun':urun
    }
    return render(request, 'detail.html', context)