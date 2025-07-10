from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/sayhi", views.sayhi, name="sayhi"),
    path("/sayhitemplate", views.sayhellowithtemplate, name="sayhitemplate"),
    path("/sayhello/<str:name>",views.sayhello, name = "sayhello"),
    path("/sayhellotemplate/<str:name>",views.sayhellotemplate, name = "sayhellotemplate"),
    path("/today",views.whatdayistoday, name = "today"),
]