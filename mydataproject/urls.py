# 路由文件
from django.conf.urls import url,include
from . import views,testdb,chart
from django.contrib import admin
urlpatterns=[
    url("hello/",views.hello),
    url("testdb/",testdb.testdb),
    url("getyuanbing/",chart.getyuanbing),
    url("tests/",include('TestModel.urls')),
    url('admin/', admin.site.urls),
      ##
    url('polls/',include('TestModel.urls')),


    ##通过250sqlserver 提取数据
    url('sqlserver/',include('sqlData.urls'))
]