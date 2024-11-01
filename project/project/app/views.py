from django.shortcuts import render,redirect
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


tudo=[{'id':'1','task':'task1'},]

def tudo1(request):
    if request.method=='POST':
        id=request.POST['id']
        task=request.POST['task']
        tudo.append({'id':id,'task':task})
        print(tudo)
        return redirect(tudo1)
    return render(request,'tudo.html',{'tudo1':tudo})

def edit_form(req,id):
    task=''
    for i in tudo:
        if i['id']==id:
            task=i
    if req.method=='POST':
        id=req.POST['id']
        task1=req.POST['task']
        task['id']=id
        task['task']=task1
        return redirect(tudo1)
    return render(req,'edit.html',{'task':task})


def delt_fun(req,id):
    for i in tudo:
        if i ['id']==id:
            tudo.remove(i)
    return redirect(tudo1)




