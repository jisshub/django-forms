from django.shortcuts import render
from . import forms
from .models import Employee
# import models here
# from formsprj.formsapp.models import Employee
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'formsapp/index.html')


def forms_view(request):
    # create an instance of Form class
    form = forms.PersonForm()
    # render form to html while pass that instance as a key:value pair
    return render(request, 'formsapp/forms.html', {'form': form})


def emp_view(request):
    empform = forms.EmployeeForm()
    if request.method == 'POST':
        # create an instance of submitted form
        form = forms.EmployeeForm(request.POST)

        # vallidate the form
        if form.is_valid():
            print('Success')
            # cleaned data means data after validation.

            empname = form.cleaned_data['empname']
            salary = form.cleaned_data['salary']
            desgin = form.cleaned_data['designation']

            # create an employee object and pass the cleaned data to each fields
            # these fields are created in models.py
            emp = Employee(empname=empname, salary=salary, designation=desgin)
            emp.save()
            messages.success(request, 'Details Saved')
    return render(request, 'formsapp/info.html', {'empform': empform})
