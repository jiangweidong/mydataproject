from django.shortcuts import render
from django.http import HttpResponse
import pymssql
import pandas as pd
from pandas import Series
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import io
import base64
import json
import time
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif': ['simhei', 'Arial']})
# 检查Python版本
from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python 3 来完成此项目')
def getdatacharts(request):
  context={}
  context["devicehot"]=imagetobase64(getDevicehot())
  plt,peoplecount,malecount,femalecount,avgtime=getfemaleandmale()
  context["femaleandmale"]=imagetobase64(plt)
  context["malecount"]=malecount
  context["peoplecount"]=peoplecount
  context["femalecount"]=femalecount
  context["avgtime"]=round(avgtime,2)
  return  render(request,'index.html',context)

def getsqlbasedata(request):
    resp = {}
    resp["data"]="change"
    peoplecount=request.GET.get("peoplecount")
    if(int(getdatalength())==int(peoplecount)):
         resp["data"]="nochange"
         return HttpResponse(json.dumps(resp), content_type="application/json")
    resp["devicehot"] = imagetobase64(getDevicehot())
    plt, peoplecount, malecount, femalecount, avgtime = getfemaleandmale()
    resp["femaleandmale"] = imagetobase64(plt)
    resp["malecount"] = malecount
    resp["peoplecount"] = peoplecount
    resp["femalecount"] = femalecount
    resp["avgtime"] = round(avgtime)
    return HttpResponse(json.dumps(resp), content_type="application/json")
def getdatalength():
    return executeSql("select count(*) as count from VisitorRecord")["count"][0]
#获取男女人数比例
def getfemaleandmale():
  fig = plt.figure()
  data1=executeSql("select * from VisitorRecord")
  maleDataFram = data1.query("GenderMale=='男'", inplace=False)
  femaleDataFrame = data1.query("GenderMale=='女'", inplace=False)
  maleCount = len(maleDataFram)
  femaleCount = len(femaleDataFrame)
  allcount = len(data1)
  labels = ["男性", "女性", "未知"]
  X = [maleCount, femaleCount, allcount - (maleCount + femaleCount)]
  plt.pie(x=X, labels=labels, autopct='%.0f%%')
  plt.title("男女人数比")
  avgtime=sum(data1['StopTime'])/len(data1)
  return plt,len(data1),len(maleDataFram),len(femaleDataFrame),avgtime
#获取机器使用热度
def getDevicehot():
    fig = plt.figure()
    dfallusecount=executeSql("select count(*) as count,IP from VisitorRecord GROUP by IP")
    dftodayusecount=executeSql("select count(*) as count,table1.ip from (select convert(varchar(100),BeginTime,23) as BeginTime,ip "
                               "from VisitorRecord where convert(varchar(100),BeginTime,23)='"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"') as table1 group by table1.ip")
    x1=dfallusecount['IP']
    value1=dfallusecount['count']
    x2 = dftodayusecount['ip']
    value2 = dftodayusecount['count']
    if(len(dfallusecount)!=len(dftodayusecount)):
        value2=value2.append(pd.Series(np.arange(len(dfallusecount)-len(dftodayusecount))))
    fig, ax = plt.subplots()
    index=np.arange(len(dfallusecount))
    bar_width=0.35
    opacity = 0.4
    rects=ax.bar(index, value1, bar_width,
                alpha=opacity, color='b',
                label='总计访问')
    rects2 = ax.bar(index+bar_width, value2, bar_width,
                  alpha=opacity, color='r',label='当天访问')
    ax.legend()
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(x1)
    fig.tight_layout()
    return plt
#传入sql获取dataframe
def executeSql(sql):
    # Create your views here.
    conn = pymssql.connect(host='117.50.5.57',
                           user='sa',
                           password='whir.2015',
                           database='GZK11QianMuDB',
                           charset='utf8')

    df0 = pd.read_sql(sql, conn)
    conn.close()
    df = pd.DataFrame(df0)

    return df
#将生成的图表转换成base64
def imagetobase64(plt):
    buffer = io.BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)
    ims = imb.decode()
    imd = "data:image/png;base64,"+ims
    return imd
