from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Flight, Airport


def index(request):
    # str1 = str(Flight.objects.all())
    context = {
        "flights": Flight.objects.all()
    }

    return render(request, "flight/index.html", context)


def flights(request, flight_id):
    try:
        flights = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "flight": flights
    }
    return  render(request, "flight/flights.html", context)
