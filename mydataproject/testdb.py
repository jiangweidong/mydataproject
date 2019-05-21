from django.http import HttpResponse
from TestModel.models import test
def testdb(request):
    test1=test(name="jiang")
    test1.save()
    return HttpResponse("<p>添加成功</p>")