from django.http import HttpResponse
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import io
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif': ['simhei', 'Arial']})
# 检查Python版本
from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python 3 来完成此项目')
def getyuanbing(request):

    lianjia_df = pd.read_excel('/Users/macbook/PycharmProjects/test/visitor.xls')
    df = lianjia_df.copy()
    df = df.drop(['ID', 'Code'], axis=1)
    # 男平均停留时间，女平均停留时间（或者人流平均停留时间）
    maleDataFram = df.query("GenderMale=='male'", inplace=False)
    femaleDataFrame = df.query("GenderMale=='female'", inplace=False)

    # maleStoptime= sum(maleDataFram.sum(axis=1)) / len(maleDataFram)
    # femaleStoptime= sum(femaleDataFrame.sum(axis=1)) / len(femaleDataFrame)
    # data1=pd.DataFrame({"平均停留时间(秒)":[maleStoptime,femaleStoptime]},index=["男性","女性"])
    # data1.plot(kind="bar",rot=0)

    # 男女比例
    maleCount = len(maleDataFram)
    femaleCount = len(femaleDataFrame)
    allcount = len(df)
    print(maleCount, femaleCount, allcount)
    labels = ["男性", "女性", "未知"]
    X = [maleCount, femaleCount, allcount - (maleCount + femaleCount)]
    plt.pie(x=X, labels=labels, autopct='%.0f%%')
    plt.title("男女人数比")

    buf=io.BytesIO()
    plt.savefig(buf,format='png')
    data3=buf.getvalue()
    response=HttpResponse(data3,content_type='image/png')
    # 一天分成上午下午两个个时间段访问占比

    # 总共访问了人流

    # 今天访问了人流

    # 平均每天访问人流

    return response