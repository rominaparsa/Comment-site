from django.shortcuts import render
#from .models import Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import User, ContactUs
from.forms import ContactUsModel
from .forms import CommentForm
import socket
# Create your views here.

def home(request):
    template = loader.get_template("Comment.html")
    #db = User(name="mohsen",family="modhej",age="36")
    #db.save()
    #result = User.objects.filter(Id=2).first()
    #context = {"name": result.name, "city": result.family, "age":result.age}
    #us = User.objects.filter(Id=1).first()
    #us.name="ali"
    #us.family="Rahimi"
    #us.save()
    #us = User.objects.filter(Id=6).first()
    #us.delete()
    return render(request=request,template_name="index1.html")
    #return HttpResponse("<h2>خوش آمدید</h2)")

def linkUser(request):
    template = loader.get_template("listUser.html")
    result =User.objects.filter(Id=2).first()
    context ={"model":result}
    return HttpResponse(template.render(context))

def index(request):
    template = loader.get_template("index.html")
    result =User.objects.all()
    context ={"model":result}
    return HttpResponse(template.render(context))


def Contact(request):
    msg = ""
    action = "/Contact"
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    if request.method == "POST":
        form = ContactUsModel(request.POST)
        if form.is_valid():
            print("فیلدهای موجود در cleaned_data: ", form.cleaned_data.keys())  # 👈 خط مهم برای دیباگ

            result = ContactUs(
                FullName=form.cleaned_data["FullName"],
                Email=form.cleaned_data["Email"],
                Message=form.cleaned_data["Message"],
                Phones=form.cleaned_data.get("Phones", ""),  # استفاده از get برای جلوگیری از ارور
                Ip=ip_address
            )
            result.save()
            return HttpResponseRedirect("/MyComment")
        else:
            msg = "اطلاعات وارد شده معتبر نیست"
    else:
        form = ContactUsModel()

    return render(request, "ContactUs.html", {
        "form": form,
        "msg": msg,
        "action": action
    })
def SaveContact(request):
    if request.method == "POST":
        forms = ContactUsModel(request.POST)
        return HttpResponse("ممنون " + forms.data["FullName"])
    return HttpResponse("لطفا فرم را از طریق POST ارسال کنید.")



def my_comment_view(request):
    form = ContactUsModel()
    MyCommentList = ContactUs.objects.all()

    context = {
        'form': form,
        'MyCommentList': MyCommentList
    }
    return render(request, 'my_comments.html', context)
#(دیگه شرط if request.method == 'POST' لازم نیست.)


def EditContact(request,id):
    result = ContactUs.objects.filter(Id=id).first()
    msg = ""
    action = "/EditSave"
    forms = ContactUsModel(initial={"Id":id,"FullName":result.FullName,"Phones":result.Phones,"Email":result.Email,"Message":result.Message})
    return render(request=request, template_name="ContactUs.html", context={"form": forms, "msg": msg,"action":action})

def EditSave(request):
    if request.method == "POST":
        forms = ContactUsModel(request.POST)
        if forms.is_valid():
            id = forms.data["Id"]
            result = ContactUs.objects.filter(Id=id).first()
            if result:
                result.FullName = forms.cleaned_data["FullName"]
                result.Email = forms.cleaned_data["Email"]
                result.Phones = forms.cleaned_data["Phones"]
                result.Message = forms.cleaned_data["Message"]
                result.save()
                return HttpResponseRedirect("/MyComment")
        return HttpResponse("داده‌های فرم معتبر نیستند")


def DeleteContact(request,id):
    result = ContactUs.objects.filter(Id=id).first()
    result.delete()
    return HttpResponseRedirect("/MyComment")

def Comment(request):
    comments = Comment.objects.all()  # گرفتن همه نظرات
    return render(request, 'your_template.html', {'MyCommentList': comments})


def getSession(request):
    return HttpResponse(request.session.get("name"))
