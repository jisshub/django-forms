from django.shortcuts import render
from .student_info import StudentForm
from .models import StudentModel


# Create your views here.

def student_view(request):
    # create an instance of form class
    newform = StudentForm()

    if request.method == 'POST':
        newform2 = StudentForm(request.POST)
        if newform2.is_valid():
            name = newform2.cleaned_data['student_name']
            course = newform2.cleaned_data['course']
            adm_no = newform2.cleaned_data['admission_no']

            student = StudentModel(Name=name, Course=course, Admission_No=adm_no)
            student.save()
    return render(request, 'studentsapp/index.html', {'form': newform})
