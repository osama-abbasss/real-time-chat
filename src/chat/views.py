from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):

    template_name = 'chat/index.html'

    return render(request, template_name)

@login_required
def room(request, room_name):

    template_name = 'chat/room.html'
    context = {
        'room_name': room_name,
        'username' : request.user.username,
        }

    return render(request, template_name, context)

def test(request):
    template_name = 'chat/2.html'
    return render(request, template_name)
