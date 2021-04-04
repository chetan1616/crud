from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentForm
from .models import Student
# Create your views here.

def StudentView(request):
    data = Student.objects.all()
    if request.method == 'POST':
        frm = StudentForm(request.POST)
        if frm.is_valid():
            nm = frm.cleaned_data['Name']
            em = frm.cleaned_data['Email']
            ps = frm.cleaned_data['Password']
            reg = Student(Name=nm, Email=em, Password=ps)
            reg.save()
            frm = StudentForm()
    else:
        frm = StudentForm()
    return render(request, 'enroll/student.html',{'forms':frm,'data':data})

def delStudent(request, id):
    stu = Student.objects.get(pk=id)
    stu.delete()
    return HttpResponseRedirect('/')

def UpdateStu(request,id):
    if request.method == 'POST':
        stu = Student.objects.get(pk=id)
        data = StudentForm(request.POST, instance=stu)
        if data.is_valid():
            data.save()
    else:
        stu = Student.objects.get(pk=id)
        data = StudentForm(instance=stu)
    return render(request,'enroll/update.html',{'data':data})

