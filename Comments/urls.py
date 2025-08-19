from django.urls import path
from . import views
from .views import my_comment_view

urlpatterns = [
    path('welcome', views.home,name="home"),
    path('linkUser', views.linkUser, name="صفحه اصلی"),
    path('', views.index, name="صفحه اصلی"),
    path('Contact', views.Contact, name="ارتباط با ما"),
    path('SaveContact', views.SaveContact, name="ارتباط با ما"),
    path('MyComment/', my_comment_view, name='my_comment'),
    path('EditContact/<int:id>', views.EditContact, name='لیست نظرات'),
    path('EditSave', views.EditSave,name="ثبت تغییرات"),
    path('DeleteContact/<int:id>', views.DeleteContact, name='حذف نظر'),
    path('getSession', views.getSession, name='حذف نظر'),
]