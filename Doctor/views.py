from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import DoctorCategory,DoctorDetails,Appointment


def index(request):
    return render(request, 'doctor/index.html')

def departments(request):
    category = DoctorCategory.objects.all()
    context = {'category' : category}
    return render(request, 'doctor/departments.html', context)

def doctors_list(request):
    doctors = DoctorDetails.objects.all()
    context = {'doctors':doctors}
    return render(request, 'doctor/doctorslist.html', context)

def doctor_details(request, doctor_name):
    person = DoctorDetails.objects.get(Name=doctor_name)
    context = {'person':person}
    return render(request, 'doctor/doctordetails.html', context)

def department_details(request, department_id):
    department = DoctorDetails.objects.filter(Specialized=department_id)
    context = {'department':department}
    return render(request, 'doctor/department details.html', context)

def submitted(request):
    appointments = Appointment.objects.all()
    context = {'appointments':appointments}
    return render(request, 'doctor/submitted.html', context)


class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['name', 'age', 'gender', 'number', 'description_of_illness', 'preferred_doctor', 'first_time_visit']



def appointment_request(request):
    return render(request, 'Doctor/appointment_success.html')

def contactus(request):
    return render(request, 'Doctor/contactus.html' )