from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django_tables2 import SingleTableView, tables, RequestConfig
# Create your views here.

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from report_swarm.models import ReportSwarmCase
from .filters import TicketFilter,OpenTicket

class ticketTable(tables.Table):
    class Meta:
        model = ReportSwarmCase
        exclude = ["description","image"]
        row_attrs = {
            "data-assignee": lambda record: record.assignee
        }

@method_decorator(login_required, name='dispatch')
class AllTicketView(SingleTableView,View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates, else redirect back to profile page

        """
        if request.user.is_superuser:
            allTickets =ReportSwarmCase.objects.all()
            CaseFilter = TicketFilter(request.GET, queryset=allTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            allTickets = CaseFilter.qs
            table = ticketTable(allTickets,template_name = "django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables":table,"filter":CaseFilter,}
            return render(request, "tickets/allTickets.html",context)
        else:
            return redirect("profile")
        
@method_decorator(login_required, name='dispatch')
class OpenTickets(SingleTableView,View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates, else redirect back to profile page

        """
        if request.user.is_superuser:
            openTickets =ReportSwarmCase.objects.filter(status="Open")
            CaseFilter = OpenTicket(request.GET, queryset=openTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            openTickets = CaseFilter.qs
            table = ticketTable(openTickets,template_name = "django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables":table,"filter":CaseFilter,}
            return render(request, "tickets/allTickets.html",context)
        else:
            return redirect("profile")

@method_decorator(login_required, name='dispatch')
class ResolvedTickets(SingleTableView,View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates, else redirect back to profile page

        """
        if request.user.is_superuser:
            resolvedTickets =ReportSwarmCase.objects.filter(status="Closed_Resolved")
            CaseFilter = OpenTicket(request.GET, queryset=resolvedTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            resolvedTickets = CaseFilter.qs
            table = ticketTable(resolvedTickets,template_name = "django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables":table,"filter":CaseFilter,}
            return render(request, "tickets/allTickets.html",context)
        else:
            return redirect("profile")

@method_decorator(login_required, name='dispatch')
class UnResolvedClosedTickets(SingleTableView,View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates, else redirect back to profile page

        """
        if request.user.is_superuser:
            closedUnresolvedTickets =ReportSwarmCase.objects.filter(status="Closed_Unresolved")
            CaseFilter = OpenTicket(request.GET, queryset=closedUnresolvedTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            closedUnresolvedTickets = CaseFilter.qs
            table = ticketTable(closedUnresolvedTickets,template_name = "django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables":table,"filter":CaseFilter,}
            return render(request, "tickets/allTickets.html",context)
        else:
            return redirect("profile")


@method_decorator(login_required, name='dispatch')
class TicketView(View):
    def get(self, request, ticketID):
        """_summary_
    if user is super user open the ticket
    if the user is not a super user but is staff check if the user is the assignee
    if the user is the assignee open the ticket
    if the user is staff but is not the assignee of the ticket redirect user back to profile page
        """

        if request.user.is_superuser:
            ticket = get_object_or_404(ReportSwarmCase,pk=ticketID)
            context = {"ticket":ticket}
            return render(request, "tickets/singularTicket.html",context)
        elif request.user.is_staff:
            ticket = get_object_or_404(ReportSwarmCase,pk=ticketID)
            if (request.user == ticket.assignee):
                context = {"ticket":ticket}
                return render(request, "tickets/singularTicket.html",context)
            else:
                return redirect("profile")
        else:
            return redirect("profile")
