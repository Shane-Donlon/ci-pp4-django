from django.shortcuts import render
from django.views import View

counties = ["Antrim","Armagh","Carlow","Cavan","Clare","Cork","Derry","Donegal","Down","Dublin","Fermanagh","Galway","Kerry","Kildare","Kilkenny","Laois","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan","Offaly","Roscommon","Sligo","Tipperary","Tyrone","Waterford","Westmeath","Wexford","Wicklow"]

from .forms import ReportSwarmForm
# Create your views here.
class ReportSwarmView(View):
    def get(self, request):
        context = {"form": ReportSwarmForm,"counties": counties}
        return render(request, "ReportSwarm/ReportSwarm.html", context)