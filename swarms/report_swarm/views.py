from django.shortcuts import render, redirect
from django.views import View
from report_swarm.models import ReportSwarmCase
from .forms import ReportSwarmForm

counties = ["Antrim", "Armagh", "Carlow", "Cavan", "Clare", "Cork", "Derry", "Donegal", "Down", "Dublin", "Fermanagh", "Galway", "Kerry", "Kildare", "Kilkenny", "Laois",
            "Leitrim", "Limerick", "Longford", "Louth", "Mayo", "Meath", "Monaghan", "Offaly", "Roscommon", "Sligo", "Tipperary", "Tyrone", "Waterford", "Westmeath", "Wexford", "Wicklow"]

# Create your views here.


class ReportSwarmView(View):
    def get(self, request):
        context = {"form": ReportSwarmForm(), "counties": counties}
        return render(request, "report_swarm/report_swarm.html", context)

    def post(self, request):
        form = ReportSwarmForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # get the last ticket logged by the user using phone number as unique identifier
            # phone used as multiple people could have the same postal code / eircode
            ticket = ReportSwarmCase.objects.filter(phone=request.POST["phone"])
            ticket = ticket.last()
            context = {"ticket": ticket }
            return render(request, "report_swarm/thanks.html",context )
        else:
            context = {"form": ReportSwarmForm(
                request.POST), "counties": counties, "errors": form.errors}
            return render(request, "report_swarm/report_swarm.html", context)
