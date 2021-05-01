from django.contrib import admin
from .models import DoctorCategory, DoctorDetails,Appointment


admin.site.register(DoctorDetails)
admin.site.register(DoctorCategory)
admin.site.register(Appointment)