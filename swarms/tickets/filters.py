from django_filters import FilterSet
from report_swarm.models import ReportSwarmCase


class TicketFilter(FilterSet):
    class Meta:
        model = ReportSwarmCase
        fields = ["status", "assignee", "first_name"]


class OpenTicket(FilterSet):
    class Meta:
        model = ReportSwarmCase
        fields = ["assignee", "first_name"]
