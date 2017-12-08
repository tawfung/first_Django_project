from django.shortcuts import render
from django.http import  HttpResponse
from first_Django_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):

    webpageslist = AccessRecord.objects.order_by("date")
    date_dict = {'access_records':webpageslist}
    return render(request,'index.html', context= date_dict)

    # my_dict={'insert_me':'I am Trace.'}
    # return render(request,'index.html',context=my_dict)