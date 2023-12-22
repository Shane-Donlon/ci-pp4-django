from django.shortcuts import render, redirect
from django.views import View
from django_tables2 import SingleTableView, tables, RequestConfig
# Create your views here.

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from report_swarm.models import ReportSwarmCase

class ticketTable(tables.Table):
    class Meta:
        model = ReportSwarmCase
        exclude = ["description","image"]
        row_attrs = {
            "data-assignee": lambda record: record.assignee
        }

@method_decorator(login_required, name='dispatch')
class SuperUserView(SingleTableView,View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates, else redirect back to profile page

        """
        if request.user.is_superuser:
            allOpenTickets =ReportSwarmCase.objects.all()
            table = ticketTable(allOpenTickets,template_name = "django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            context = {"tables":table}
            return render(request, "tickets/tickets.html",context)
        else:
            return redirect("profile")
        
        
