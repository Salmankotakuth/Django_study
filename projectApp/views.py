from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def index(request):
    return render(request, 'index.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'projectApp/add_student.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'projectApp/student_list.html', {'students': students})