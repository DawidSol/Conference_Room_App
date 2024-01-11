from django.http import HttpResponse
from django.shortcuts import render
from .models import Room


def home_page(request):
    return render(request, "base.html")


def add_new_room(request):
    if request.method == "GET":
        return render(request, "new_room.html")
    else:
        name = request.POST["name"]
        capacity = request.POST["capacity"]
        projector = request.POST.get("projector")
        if not name:
            return HttpResponse("You must provide a name!")
        elif Room.objects.filter(name=name).exists():
            return HttpResponse("Room with this name already exists!")
        elif int(capacity) <= 0:
            return HttpResponse("Capacity must be greater than 0!")
        elif not projector:
            return HttpResponse("You must specify if there is a projector or not!")
        else:
            new_room = Room(name=name, capacity=capacity, projector_available=projector)
            new_room.save()
            return render(request, "base.html")
