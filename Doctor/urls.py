from django.urls import path

from . import views

app_name = 'doctors'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),

    path('departments/', views.departments, name='departments'),
    path('departments/<int:department_id>/', views.department_details, name='department_details'),

    path('doctors/', views.doctors_list, name='doctors_list'),
    path('doctors/<str:doctor_name>/', views.doctor_details, name='doctor_details'),

    #appointment/
    path('appointment/', views.AppointmentCreate.as_view(), name='appointment'),
    path('appointment_request', views.appointment_request, name='appointment_request'),


    path('submitted/', views.submitted, name='submitted'),

    path('contact_us/', views.contactus, name='contact_us'),

]
