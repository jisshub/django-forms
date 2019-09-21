from django import forms


class PersonForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter Email: ')
    text = forms.CharField(widget=forms.Textarea)


class EmployeeForm(forms.Form):
    empname = forms.CharField()
    salary = forms.IntegerField()
    designation = forms.CharField()

