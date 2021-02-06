from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Kriskras, Vergadering
from .form import CreateKriskras

# Create your views here.

def index(response, id):
    kriskras = Kriskras.objects.get(id=id)
    
    if response.method == "POST":
        print(kriskras)
        if response.POST.get("wijzig"):
            print("wijzig")
            for vergadering in kriskras.vergadering_set.all():
                    pass
                    

        elif response.POST.get("newVergadering"):
            txt = response.POST.get("new")
            date = response.POST.get("newdate")

            if len(txt) > 2:
                kriskras.vergadering_set.create(activiteit=txt, date=date)
            else:
                print("invalid")

    return render(response, "main/kriskras.html", {"kriskras":kriskras})

def home(response):
    ls = Kriskras.objects.all()
    return render(response, "main/home.html", {"ls":ls})

def create(response):
    if response.method == "POST":
        form = CreateKriskras(response.POST)

        if form.is_valid():
            n = form.cleaned_data["tak"]
            t = Kriskras(tak = n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateKriskras()
    return render(response, "main/create.html", {"form":form})
