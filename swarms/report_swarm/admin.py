from django.contrib import admin
from .models import ReportSwarmCase
# Register your models here.

@admin.register(ReportSwarmCase)

class SwarmAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "email", "createdOn"]
    list_filter = ["createdOn"]
    search_fields = ["first_name", "email", "description"]
    actions = ["approve_comments"]