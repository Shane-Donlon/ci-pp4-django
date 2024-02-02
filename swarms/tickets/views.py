import json

from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import Http404, JsonResponse, HttpResponse,HttpResponseForbidden 
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views import View
from django_tables2 import RequestConfig, SingleTableView
from report_swarm.models import ReportSwarmCase
from django.core.serializers import serialize
from .filters import OpenTicket, TicketFilter
from .tables import ticketTable
from django.contrib import messages
from django.db.models import Q

# Create your views here.

UNASSIGNED_USER = 3

@method_decorator(login_required, name='dispatch')
class AllTicketView(SingleTableView, View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates,

        """
        if request.user.is_superuser:
            allTickets = ReportSwarmCase.objects.all()
            CaseFilter = TicketFilter(request.GET, queryset=allTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            allTickets = CaseFilter.qs
            table = ticketTable(
                allTickets, template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables": table, "filter": CaseFilter, }
            return render(request, "tickets/allTickets.html", context)
        else:
            return redirect("profile")


@method_decorator(login_required, name='dispatch')
class OpenTickets(SingleTableView, View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates,  else get a list of tickets assigned to the login user status open

        """
        openTickets = ReportSwarmCase.objects.filter(status="Open" )
        if request.user.is_superuser:
            CaseFilter = OpenTicket(request.GET, queryset=openTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            openTickets = CaseFilter.qs
            table = ticketTable(
                openTickets, template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables": table, "filter": CaseFilter, }
            return render(request, "tickets/allTickets.html", context)
        elif request.user.is_staff:
            # assignee 3 === unassigned
            openTickets = openTickets.filter(Q(assignee=request.user)|Q(assignee=3))
            table = ticketTable(
                openTickets, template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables": table, }
            return render(request, "tickets/allTickets.html", context)
        else:
            return redirect("profile")


@method_decorator(login_required, name='dispatch')
class ResolvedTickets(SingleTableView, View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates, else redirect back to profile page

        """
        resolvedTickets = ReportSwarmCase.objects.filter(
            status="Closed_Resolved")
        if request.user.is_superuser:

            CaseFilter = OpenTicket(request.GET, queryset=resolvedTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            resolvedTickets = CaseFilter.qs
            table = ticketTable(
                resolvedTickets, template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables": table, "filter": CaseFilter, }
            return render(request, "tickets/allTickets.html", context)
        elif request.user.is_staff:
            resolvedTickets = resolvedTickets.filter(assignee=request.user)
            table = ticketTable(
                resolvedTickets, template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables": table, }
            return render(request, "tickets/allTickets.html", context)
        else:
            return redirect("profile")


@method_decorator(login_required, name='dispatch')
class UnResolvedClosedTickets(SingleTableView, View):
    def get(self, request):
        """_summary_
    if user is super user go to all tickets templates, else redirect back to profile page

        """
        closedUnresolvedTickets = ReportSwarmCase.objects.filter(
            status="Closed_Unresolved")
        if request.user.is_superuser:
            CaseFilter = OpenTicket(
                request.GET, queryset=closedUnresolvedTickets)
            # if there is a filtered queryset we are remaking the variable data with the filtered data
            closedUnresolvedTickets = CaseFilter.qs
            table = ticketTable(
                closedUnresolvedTickets, template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables": table, "filter": CaseFilter, }
            return render(request, "tickets/allTickets.html", context)
        elif request.user.is_staff:
            closedUnresolvedTickets = closedUnresolvedTickets.filter(
                assignee=request.user)
            table = ticketTable(
                closedUnresolvedTickets, template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"tables": table, }
            return render(request, "tickets/allTickets.html", context)
        else:
            return redirect("profile")


@method_decorator(login_required, name='dispatch')
class TicketView(View):
    def get(self, request, ticketID):
        """_summary_
    if user is super user open the ticket
    if the user is the assignee open the ticket
    if the user is logged in but is not the assignee raise 404
        """
        ticket = get_object_or_404(ReportSwarmCase, pk=ticketID)
   
        if  request.user.is_superuser or request.user == ticket.assignee or ticket.assignee.username == "unassigned":
            
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                ticket = ReportSwarmCase.objects.filter(pk=ticketID)
                ticket = serialize("json", ticket)
                ticket = json.loads(ticket)

                return JsonResponse({"ticket":ticket})
            else:
                superUser = User.objects.filter(is_superuser=True)
                currentUser = request.user
                context = {"ticket": ticket,
                           "superUser":superUser,"currentUser":currentUser}
                return render(request, "tickets/singularTicket.html", context)
        else:
            raise Http404

    def post(self, request, ticketID):
        ticket = get_object_or_404(ReportSwarmCase, pk=ticketID)
        postTicket =  json.loads(request.body)
        postTicket = postTicket["ticket"]

        try:
            assignee = User.objects.filter(username=postTicket["assignee"])[0]
            ticket.first_name = postTicket["first_name"]
            ticket.last_name = postTicket["last_name"]
            ticket.phone = postTicket["phone"]
            ticket.email = postTicket["email"]
            ticket.address = postTicket["address"]
            ticket.town = postTicket["town"]
            ticket.county = postTicket["county"]
            ticket.eircode = postTicket["eircode"]
            ticket.location = postTicket["location"]
            ticket.description = postTicket["description"]
            ticket.assignee =   assignee
            ticket.status = postTicket["status"]
      

            ticket.save()

            message = "saved"
            message = JsonResponse({"message":message})
    
            return HttpResponse(message, content_type='text/plain')
        except:
            message = "invalid"

            message = JsonResponse({"message":message})
            return HttpResponse(message, content_type='text/plain')


    def delete(self, request, ticketID):
        if request.user.is_superuser:
            ticket = get_object_or_404(ReportSwarmCase, pk=ticketID)
            ticket.delete()
            message = "delete"
            message = JsonResponse({"message":message})
            return HttpResponse(message, content_type='text/plain')
        
        else:
            HttpResponseForbidden()