from django.shortcuts import render
from django.views import View
from .forms import ReportSwarmCase
counties = ["Antrim","Armagh","Carlow","Cavan","Clare","Cork","Derry","Donegal","Down","Dublin","Fermanagh","Galway","Kerry","Kildare","Kilkenny","Laois","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan","Offaly","Roscommon","Sligo","Tipperary","Tyrone","Waterford","Westmeath","Wexford","Wicklow"]

from .forms import ReportSwarmForm
# Create your views here.
class ReportSwarmView(View):
    def get(self, request):
        context = {"form": ReportSwarmForm,"counties": counties}
        return render(request, "report_swarm/report_swarm.html", context)
    
    def post(self, request):
        form = ReportSwarmCase(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            return render(request, "report_swarm/thanks.html", )
        context = {"form": ReportSwarmForm(request.POST),"counties": counties}
        return render(request, "report_swarm/report_swarm.html", context )