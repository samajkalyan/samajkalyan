# form_app/models.py

from django.db import models
import uuid

class FormData(models.Model):
    unique_id = models.CharField(max_length=6, unique=True,null=True)  # Unique ID field
    serial_no = models.IntegerField(unique=True,null=True)  # Serial number field
    salutation = models.CharField(max_length=100,null=True)
    first_name = models.CharField(max_length=100,null=True)
    middle_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100)
    taluka = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    whatsapp_no = models.CharField(max_length=15)
    num_family_members = models.IntegerField()
    aadhar_no = models.CharField(max_length=30)
    Type_of_members = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True,auto_now_add=True)

