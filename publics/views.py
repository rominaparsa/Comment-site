from django.shortcuts import render, redirect
from django.http import HttpResponse
from .UserAuth import UserAuth
from .models import ask
from .forms import askedForm
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
#from datetime as DateTime

def panel(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        form = askedForm()
        listmyask = ask.objects.filter(User_id=user_st["User"].id).all()
        return render(request, "panel.html", {
            "user_st": user_st,
            "listmyask": listmyask,
            "form": form
        })
    else:
        return HttpResponse("عدم دسترسی به این صفحه 403")


def GetMyAsked(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        print(user_st["User"].id)
        listmyask = ask.objects.filter(user_id = user_st["User"].id).all()
        for item in listmyask:
            print(item.title)
        return HttpResponse(str(listmyask))
    else:
        return HttpResponse("عدم دسترسی به این صفحه 403")


def saveAsk(request):
    user_st = UserAuth().StateLogin(request)
    if not user_st["State"]:
        return HttpResponse("false")

    if request.method == "POST":
        form = askedForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ask_id = request.POST.get("ask_id")

            try:
                if ask_id and ask_id != "0":
                    # ویرایش سوال
                    question = ask.objects.get(Id=ask_id, User=user_st['User'])
                    # بررسی اینکه سوال تکراری نباشه به جز سوال خودش
                    duplicate = ask.objects.filter(title=data["title"]).exclude(Id=ask_id).exists()
                    if duplicate:
                        return HttpResponse("exists")

                    question.title = data['title']
                    question.caption = data['caption']
                    question.save()
                else:
                    # افزودن سوال جدید
                    if ask.objects.filter(title=data["title"]).exists():
                        return HttpResponse("exists")

                    ask.objects.create(
                        caption=data['caption'],
                        title=data['title'],
                        User=user_st['User'],
                        Created=timezone.now()
                    )
                return HttpResponse("true")
            except:
                return HttpResponse("false")
        else:
            return HttpResponse("false")
    return HttpResponse("false")

def deletAsk(request):
    user_st = UserAuth().StateLogin(request)
    if not user_st["State"]:
        return HttpResponse("403")

    if request.method == "POST":
        ask_id = request.POST.get("ask_id")
        try:
            question = ask.objects.get(Id=ask_id, User=user_st["User"])
            question.delete()
            return HttpResponse("true")
        except:
            return HttpResponse("false")
    return HttpResponse("false")

def readallAsk(request):
    if request.method == "POST":
        if str(request.POST.get("tokens"))=="milas22@@#na2#&%*@#+/2/":
            user_st = UserAuth().StateLogin(request)
            if user_st["State"]:
                search = request.POST.get("search")

                if search!="":
                    listData = ask.objects.filter(User_id=user_st["User"].id,title__contains=search).all()
                else:
                    listData = ask.objects.filter(User_id=user_st["User"].id).all()

                myserData = serializers.serialize("json",listData)
                return HttpResponse(myserData)
    return HttpResponse("403")