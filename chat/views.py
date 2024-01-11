from django.shortcuts import render, HttpResponse
from .models import User
from .models import Chat
from django.db.models import Q
from chat.consumers import ChatConsumer
from django.views.decorators.csrf import csrf_exempt


def index(request):
    User_list  = User.objects.all()
    return render(request, 'chat/index.html',{
        'user_list': list(User_list)
    })


def room(request, room_name):
    try:
        sender = User.objects.get(username = room_name)
        chats = Chat.objects.filter(Q(sender__username__icontains=sender.username) | Q(reciver__username__contains=sender.username))
        old_chat = ""
        for chat in chats[:10]:
            old_chat = old_chat + " \n " +  chat.messages + "\n" + str(chat.created_at)
        chats = Chat.objects.filter(reciver = sender)
        for chat in chats[:10]:
            old_chat = old_chat + " \n " +  chat.messages + "\n" + str(chat.created_at)
        return render(request, 'chat/room.html', {
            "old_chats": chats,
            'room_name': room_name
        })
    except User.DoesNotExist:
        User_list  = User.objects.all()
        return render(request, 'chat/room.html', {
            "no_found": True,
            'room_name': room_name,
            'user_list': list(User_list)
        })
    except:
        User_list  = User.objects.all()
        return render(request, 'chat/room.html', {
            "no_found": True,
            'room_name': room_name,
            'user_list': list(User_list)
        })

@csrf_exempt
def reply(request, room_name):
    if request.method == 'POST':
        try:
            print("in reply")

            if 'message' in request.POST:
                print("got message")
                message = request.POST['message']
                scope = {"url_route":{"kwargs":{"room_name":room_name}}}
                chat_consumner = ChatConsumer
                chat_consumner.send_job_notification(room_name=room_name,message=message)
                return render(request, 'chat/list_user.html', {
                    'message': message
                })
        except Exception as e:
            print(e)
            return render(request, 'chat/list_user.html', {
                    'message': str(e)
                })
            
        


def users_available(request):
    User_list  = User.objects.all()
    return render(request, 'chat/list_user.html', {
        'user_list': list(User_list)
    })

def ChatUpdate(request):
    if request.method == 'POST':
        if 'message' in request.POST:
            message = request.POST['message']
            print(f" meaages {message}")
            reciver = User.objects.get(username = request.POST['reciver'])
            New_chat = Chat.objects.create(
                sender = request.user,
                reciver = reciver,
                messages = message
            )
            New_chat.save()
        return HttpResponse('success') 



# Create your views here.
