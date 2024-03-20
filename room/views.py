from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})

@login_required
def createRoom(request):
    if request.method == "POST":
        form=RoomForm(data=request.POST)
        if form.is_valid():
            form.save()
            # obj=form.instance
            return redirect('rooms')
    else:
        form = RoomForm()
        return render(request,"room/addroom.html",{"form":form})
