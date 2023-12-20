from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]
        labels = {"first_name": "First Name",
                  "last_name": "Last Name"}
