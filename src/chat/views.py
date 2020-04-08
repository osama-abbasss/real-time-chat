from django.shortcuts import render

def index(request):

    template_name = 'chat/index.html'
    
    return render(request, template_name)


def room(request, room_name):

    template_name = 'chat/room.html'
    context = {
        'room_name': room_name
        }

    return render(request, template_name, context)
