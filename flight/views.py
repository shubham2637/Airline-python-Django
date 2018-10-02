from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Flight


def index(request):
    context = {
        "flights": Flight.objects.all()
    }

    return render(request,"flight/index.html", context)

