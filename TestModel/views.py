from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    return HttpResponse("你正在看问题 %s" %question_id)
def results(request,quetion_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % quetion_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)