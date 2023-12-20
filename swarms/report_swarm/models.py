from django.db import models
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

StatusOptions = [("Open","Open"),("Closed_Resolved","Resolved"),("Closed_Unresolved","Unable to Resolve")]


class ReportSwarmCase(models.Model):
    # form information for Model Form
    first_name = models.CharField(max_length=60, null=True, blank=False, )
    last_name = models.CharField(max_length=60, null=True, blank=False)
    phone =  models.CharField(max_length=60, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True,blank=False)
    address1 = models.CharField(max_length=60, null=True,blank=False)
    address2 = models.CharField(max_length=60, null=True,blank=False)
    address3 = models.CharField(max_length=60, null=True, blank=True)
    county = models.CharField(max_length=60, null=True, blank=False)
    eircode = models.CharField(max_length=8, null=True, blank=False,)
    location = models.CharField(max_length=8,choices = [("outside", "Outside"), ("inside", "Inside")])
    description = models.TextField(max_length=10000, null=True, blank=False)
    image = CloudinaryField('image')
    createdOn = models.DateTimeField(auto_now_add=True, )
    updatedOn = models.DateTimeField(auto_now=True,)
    status = models.CharField(choices =StatusOptions,default="Open",max_length=100 )
    assignee = models.OneToOneField(User, on_delete=models.CASCADE,default = 3,related_name="assignee")
    # UPDATE DEFAULT ASSIGNEE
    
    