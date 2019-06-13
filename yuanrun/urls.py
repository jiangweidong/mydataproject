from django.urls import  path
from . import  views
urlpatterns=[
    # 获取K11数据报表
    path('getdatacharts/',views.getdatacharts,name='getdatacharts'),
    path('getsqlbasedata/',views.getsqlbasedata,name='getsqlbasedata')
]