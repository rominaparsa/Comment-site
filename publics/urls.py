from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.panel, name="panel"),
    path('dataajaxs/readAsk', views.readallAsk, name="readAsk"),
    path('dataajaxs/saveAsk', views.saveAsk, name="saveAsk"),
    path('dataajaxs/deletAsk', views.deletAsk, name="deletAsk"),
]


