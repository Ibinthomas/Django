from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return HttpResponse("fun1 demo data")


def fun2(request):
    a={'name':'manu', 'age':20}
    return HttpResponse(a)

def fun3(req,a,b):
    return HttpResponse(a)

def fun4(req,a,b,c):
    if a>b and a>c:
        return HttpResponse(a)
    elif b>a and b>c:
        return HttpResponse(b)
    else:
        return HttpResponse(c)

def index_page(req):
    name='ibin'
    age=20
    place='kozhikode'
    return render(req,'index.html',{'name':name,'age':age,'place':place})

def demo(req):
    l=[{'name':'aa','age':23},{'name':'bbb','age':22},{'name':'ccs','age':22}]
    d={'name':'aaa','age':23}
    return render(req,'demo.html',{"data":l,'data1':d})

def second(req):
    return render(req,'second.html')