from django.http import HttpResponse
from django.shortcuts import render, redirect
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
        elif not capacity:
            return HttpResponse("You must provide room capacity!")
        elif int(capacity) <= 0:
            return HttpResponse("Capacity must be greater than 0!")
        elif not projector:
            return HttpResponse("You must specify if there is a projector or not!")
        else:
            new_room = Room(name=name, capacity=capacity, projector_available=projector)
            new_room.save()
            return render(request, "base.html")


def rooms_list(request):
    rooms = Room.objects.all()
    if not rooms:
        return HttpResponse("No rooms found!")
    else:
        return render(request, "rooms_list.html", {"rooms": rooms})


def room_name(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        return render(request, 'room_name.html', {"room": room})
    except Room.DoesNotExist:
        return HttpResponse("Room does not exist!")


def delete_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        return HttpResponse("Room does not exist!")
    if request.method == 'GET':
        room.delete()
        return redirect('main_app:rooms_list')


def modify_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        return HttpResponse("Room does not exist!")
    if request.method == 'GET':
        return render(request, 'modify_room.html',)
    else:
        changed_name = request.POST["name"]
        changed_capacity = request.POST["capacity"]
        changed_projector = request.POST.get("projector")
        if not changed_name:
            return HttpResponse("You must provide a name!")
        elif Room.objects.filter(name=changed_name).exists():
            return HttpResponse("Room with this name already exists!")
        elif not changed_capacity:
            return HttpResponse("You must provide room capacity!")
        elif int(changed_capacity) <= 0:
            return HttpResponse("Capacity must be greater than 0!")
        elif not changed_projector:
            return HttpResponse("You must specify if there is a projector or not!")
        else:
            room.name = changed_name
            room.capacity = changed_capacity
            room.projector = changed_projector
            room.save()
            return render(request, "base.html")
