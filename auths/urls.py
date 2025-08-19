from django.urls import path
from . import views
#from .views import my_comment_view

urlpatterns = [
    path('', views.logins,name="home"),
    path('register', views.register, name="home"),
    path('Checklogin', views.Checklogin, name="home"),
    path('setSession', views.setSession, name="home"),
    path('setCookies', views.setCookies, name="home"),
    path('getCookies', views.getCookies, name="home"),
    path('registerAction', views.registerAction, name="home"),
    path('CheckAuth', views.CheckAuth, name="CheckAuth"),
    path('logOut', views.logOut, name="logOut"),
]