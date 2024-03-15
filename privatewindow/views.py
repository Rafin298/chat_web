from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Mychats
# from .models import Room, Message

@login_required
def privateWindow(request):
    all_users= get_user_model().objects.exclude(username=request.user.username)
    context= {'allusers': all_users}
    return render(request, 'privatewindow/index.html', context)
    # return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def chatroom(request, frndname):
    frnd_name = User.objects.get(username=frndname)
    myname = request.user
    # myname =User.objects.get(username=mynames)
    print(myname.username,frnd_name.username)
    messages = Mychats.objects.filter(me=frnd_name, frnd=myname) | Mychats.objects.filter(me=myname, frnd=frnd_name)
    print(messages)
    return render(request, 'privatewindow/chatroom.html', {'frndname':frnd_name,'messages': messages})
