from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    context={}
    context['hello']="zhouchunssssss"
    return render(request,'hello.html',context)