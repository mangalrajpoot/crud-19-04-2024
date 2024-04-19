from django.shortcuts import render,redirect
from .models import User 

# Create your views here.
def create(request):
    if request.method=='GET':
        return render(request,'home/create.html')
    else:
        fullname=request.POST['fullname']
        gender=request.POST['g']
        email=request.POST['email']
        course=request.POST.getlist('c')
        city=request.POST['city']
        data=User(fullname=fullname, gender=gender, email=email,course=course, city=city)
        data.save()
        context={'m':'Data Inserted Successfully'}
        return render(request,'home/create.html',context)
    

def read(request):
    n=User.objects.all() #
    context={'data':n}
    return render(request,'home/read.html',context)

def edit(request):
    id=request.GET['q']
    newdata=User.objects.get(id=id)
    if request.method=='GET':
        return render(request,'home/edit.html',{'data':newdata})
    else:
        newdata.fullname=request.POST['fullname']
        newdata.gender=request.POST['g']
        newdata.email=request.POST['email']
        newdata.course=request.POST.getlist('c')
        newdata.city=request.POST['city']
        newdata.save()
        return redirect('read')
    

def delete(request):
    id=request.GET['q']
    newdata=User.objects.get(id=id)
    if request.method=='GET':
        return render(request,'home/delete.html',{'data':newdata})
    else:
        
        newdata.delete()
        
        return redirect('/')

    





