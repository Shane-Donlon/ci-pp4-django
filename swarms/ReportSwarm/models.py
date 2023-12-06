from django.db import models
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField


# County_Choices = [("Antrim","Antrim"),("Armagh","Armagh"),("Carlow","Carlow")]
# "Antrim","Armagh","Carlow","Cavan","Clare","Cork","Derry","Donegal","Down","Dublin","Fermanagh","Galway","Kerry","Kildare","Kilkenny","Laois","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan","Offaly","Roscommon","Sligo","Tipperary","Tyrone","Waterford","Westmeath","Wexford","Wicklow"
# Create your models here.
class ReportSwarmCase(models.Model):
    # form information for Model Form
    first_name = models.CharField(max_length=60, null=True, blank=False, )
    last_name = models.CharField(max_length=60, null=True, blank=False)
    phone =  PhoneNumberField(max_length=12, blank=False, region="IE")
    email = models.EmailField(max_length=254, null=True,blank=False)
    address1 = models.CharField(max_length=60, null=True,blank=False)
    address2 = models.CharField(max_length=60, null=True,blank=False)
    address3 = models.CharField(max_length=60, null=True, blank=True)
    county = models.CharField(max_length=60, null=True, blank=False)
    eircode = models.CharField(max_length=8, null=True, blank=False,validators=[MinLengthValidator(7),])
    location = models.CharField(max_length=8,choices = [("outside", "Outside"), ("inside", "Inside")])
    description = models.TextField(max_length=10000, null=True, blank=False)
    image = CloudinaryField('image')
    createdOn = models.DateTimeField(auto_now_add=True, )
    updatedOn = models.DateTimeField(auto_now=True,)