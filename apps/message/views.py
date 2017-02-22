# __*__ coding:utf-8 __*__
from django.shortcuts import render
from .models import UserMessage


# Create your views here.
def getform(request):
    message = None
    all_message = UserMessage.objects.all().filter(name='bobbytest')  # 把数据库记录全部返回
    # for message in all_message:
    #     message.delete()
    #     print(message.name)
    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "hellowrd2"
    #     user_message.save()
    if all_message:
        message = all_message[0]
        print(message.email+"??")

    return render(request, 'message_form.html',{"my_message":message})
