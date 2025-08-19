from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Login,Register
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def logins(request):
     forms = Login()
     return render(request=request,template_name="login.html",context={"form":forms})

def register(request):
     forms = Register()
     return render(request=request,template_name="register.html",context={"form":forms})

def Checklogin(request):
     forms = Login(request.POST)
     if forms.is_valid():
          username = forms.data["UserName"]
          password = forms.data["Password"]
          user = authenticate(request,username=username,password=password)
          if user is not None:
               login(request,user)
               return HttpResponseRedirect("/panel")
          else:
               return HttpResponse("حسابی با این مشخصات یافت نشد")

def setSession(request):
     request.session["name"]="milad"
     return HttpResponseRedirect("/getSession")


def setCookies(request):
     response = HttpResponse()
     response.set_cookie("UserName","milad")
     return response

def getCookies(request):
    user_name = request.COOKIES.get("UserName")
    if user_name:
        return HttpResponse(user_name)
    else:
         return HttpResponse("کوکی یافت نشد")

def registerAction(request):
     if request.method == "POST":
          forms = Register(request.POST)
          if forms.is_valid():
               users = User.objects.filter(username=forms.data["UserName"])
               if users.count() > 0:  # اصلاح این خط
                    return HttpResponse("این کاربر در سیستم وجود دارد")
               else:
                    us = User.objects.create_user(forms.data["UserName"], "test@gmail.com", forms.data["Password"])
                    us.first_name = forms.data["Name"]
                    us.last_name = forms.data["Family"]
                    us.save()
               return HttpResponse("کاربر ساخته شد")
          else:
               return HttpResponse("فرم نا معتبر است")

def CheckAuth(request):
     if request.user.is_authenticated:
          return HttpResponse("وارد شده است")
     else:
          return HttpResponse("وارد نشده است")

def logOut(request):
     logout(request)
     return HttpResponseRedirect("/auth/")
