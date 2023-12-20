from django.forms import ModelForm
from .models import ReportSwarmCase
class ReportSwarmForm(ModelForm):

    class Meta:
        model = ReportSwarmCase
        fields = "__all__"
        exclude= ["status","assignee"]
        labels = {"first_name": "First Name",
                  "last_name": "Last Name"}
