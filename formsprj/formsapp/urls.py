from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms_view, name='forms'),
    path('employee/', views.emp_view, name='forms2')
]
