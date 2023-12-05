from django.forms import ModelForm
from .models import ReportSwarmCase
class ReportSwarmForm(ModelForm):

    class Meta:
        model = ReportSwarmCase
        fields = "__all__"
        labels = {"first_name": "First Name",
                  "last_name": "Last Name"}
