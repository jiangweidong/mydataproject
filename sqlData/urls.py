from django.urls import  path
from . import views
urlpatterns=[
    path('getdatacharts/',views.getdatacharts,name='getdatacharts')
]