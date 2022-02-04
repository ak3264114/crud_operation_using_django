from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from student_info.models import Student

# Create your views here.
def index(request):
    all_stu = Student.objects.all()
    return render(request,'index.html', {"all_stu":all_stu})

def add(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        std = request.POST['std']
        sec = request.POST['sec']
        Student(name=name , email=email , std=std , sec=sec ,).save()
        return HttpResponse('added Succesfully <br/> <br/> <br/> <a href="/" style="border: 3px solid #00dcff; padding: 3px 10px;background-color: #91ff00ba;border-radius: 10px;" role="button" role="button">Go Back</a>')

    else:
        return render(request,'index.html')


def remove(request,stu_id):
    if stu_id :
        try:        
           Student.objects.get(id=stu_id).delete()
           return HttpResponse('Removed Succesfully <br/> <br/> <br/> <a  href="/" role="button" style="border: 3px solid #00dcff; padding: 3px 10px;background-color: #91ff00ba;border-radius: 10px;" role="button" >Go Back</a>')
        except:
            Student.objects.get(id=stu_id).delete()
            return render(request,'index.html')

def edit(request , edit_id) :
    student_data = Student.objects.get(id=edit_id)
    return render(request,'edit.html', {"student_data":student_data})

def update(request,update_id):
    if request.method=='POST':
        upd_std = Student.objects.get(id=update_id)
        upd_std.name = request.POST.get('name')
        upd_std.email = request.POST.get('email')
        upd_std.std = request.POST.get('std')
        upd_std.sec = request.POST.get('sec')
        upd_std.save()
        all_stu = Student.objects.all()
        return HttpResponse('Update Succesfully <br/> <br/> <br/> <a href="/" style="border: 3px solid #00dcff; padding: 3px 10px;background-color: #91ff00ba;border-radius: 10px;" role="button">Go Back</a>')