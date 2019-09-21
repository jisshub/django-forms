from django import forms


class StudentForm(forms.Form):
    student_name = forms.CharField()
    course = forms.CharField()
    admission_no = forms.IntegerField()
