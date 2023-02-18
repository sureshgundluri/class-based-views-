from django.shortcuts import render
from app.forms  import *
from app.models import *
from django.http import HttpResponse
from django.views.generic import View

def insert_topic(request):
    tfo=Topicform()
    d={'form':tfo}
    if request.method=='POST':
        TFD=Topicform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted successfully')
    return render(request,'insert_topic.html',d)

class CBVinsert_webpage(View):
    def get(self,request):
        wfo=Webpageform()
        d={'form':wfo}
        return render(request,'CBVinsert_webpage.html',d)
    def post(self,request):
        WFD=Webpageform(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('data is inserted  successfullly')
