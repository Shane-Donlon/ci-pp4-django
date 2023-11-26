from django.db import models

COUNTIES = (
       ('available', ('Available to borrow')),
       ('borrowed', ('Borrowed by someone')),
       ('archived', ('Archived - not available anymore')),
   )
# Create your models here.
class ReportSwarmCase(models.Model):
    # form information for Model Form
    first_name = models.CharField(max_length=60, null=True, blank=False,)
    last_name = models.CharField(max_length=60, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True,blank=False)
    address1 = models.CharField(max_length=60, null=True,blank=False)
    address2 = models.CharField(max_length=60, null=True,blank=False)
    address3 = models.CharField(max_length=60, null=True, blank=True)
    county = models.CharField(max_length=60, null=True, blank=True)
    eircode = models.CharField(max_length=8, null=True, blank=False)