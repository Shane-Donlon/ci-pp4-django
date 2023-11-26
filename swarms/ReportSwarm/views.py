from django.shortcuts import render
from django.views import View


from .forms import ReportSwarmForm
# Create your views here.
class ReportSwarmView(View):
    def get(self, request):
        context = {"form": ReportSwarmForm}
        return render(request, "ReportSwarm/ReportSwarm.html", context)