from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from .models import Flight, Passenger


def index(request):
    # str1 = str(Flight.objects.all())
    context = {
        "flights": Flight.objects.all()
    }

    return render(request, "flight/index.html", context)


def flights(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "flights": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flight/flights.html", context)


def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flight/error.html", {"message":"No slection made."})
    except Passenger.DoesNotExist:
        return render(request, "flight/error.html", {"message":"No passenger."})
    except Flight.DoesNotExist:
        return render(request, "flight/error.html", {"message":"No flight."})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flights", args=(flight_id,)))
