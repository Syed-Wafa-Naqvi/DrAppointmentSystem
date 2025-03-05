from django.db import models
import datetime

# Create your models here.
class BaseAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Doctor(BaseAbstract):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    available_time = models.TimeField(default=datetime.time(9, 0))
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Appointment(BaseAbstract):
    patient_name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.patient_name