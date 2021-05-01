from django.db import models
from django.urls import reverse



class DoctorCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


Gender = (
    ('male', 'male'),
    ('female', 'female'),
    ('others', 'others'),
)


class DoctorDetails(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(blank=True,null=True)
    Address = models.CharField(max_length=500, blank=True, null=True)
    Phone_no = models.CharField(max_length=11)
    Degree = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True, choices=Gender)
    Time = models.CharField(max_length=100)
    Room_no = models.CharField(max_length=10)
    Fees = models.PositiveIntegerField()
    Specialized = models.ForeignKey(DoctorCategory, on_delete=models.CASCADE)
    Short_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Name

Visit = (
    ('Yes','Yes'),
    ('No', 'No'),
)

Status = (
    ('Pending','Pending'),
    ('Confirmed', 'Confirmed'),
)




class Appointment(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices=Gender)
    number = models.CharField(max_length=11)
    description_of_illness = models.CharField(max_length=2000)
    preferred_doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    first_time_visit = models.CharField(max_length=20, choices=Visit)
    status = models.CharField(max_length=20, choices=Status, null=True, blank=True, default='Pending')

    def get_absolute_url(self):
        return reverse('doctors:appointment_request')



    def __str__(self):
        return self.name

