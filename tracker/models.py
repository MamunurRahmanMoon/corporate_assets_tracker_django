from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Device(models.Model):
    name = models.CharField(max_length=255)
    current_employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField()
    check_in_time = models.DateTimeField(null=True, blank=True)
    condition_out = models.CharField(max_length=255)
    condition_in = models.CharField(max_length=255, null=True, blank=True)
