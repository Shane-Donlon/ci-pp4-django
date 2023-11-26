from django.shortcuts import render
from django.views import View
# Create your views here.
class ReportSwarmView(View):
    def get(self, request):
        return render(request, "ReportSwarm/ReportSwarm.html")