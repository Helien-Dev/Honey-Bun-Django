from django.shortcuts import render


# Create your views here.
def bun_Home(request):
    context = {"title": "Honey Bun Shop", "description": "Home page of Honey Bun Shop"}
    return render(request, "bun_home.html", context)
