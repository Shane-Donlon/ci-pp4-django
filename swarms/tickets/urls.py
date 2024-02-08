from django.urls import path

from . import views

urlpatterns = [
    path("all", views.AllTicketView.as_view(), name="all_tickets"),
    path("status/open", views.OpenTickets.as_view(), name="open_tickets"),
    path("status/resolved",
         views.ResolvedTickets.as_view(), name="resolved_tickets"),
    path("status/closed-not-solved",
         views.UnResolvedClosedTickets.as_view(), name="unresolved_tickets"),
    path("<int:ticketID>", views.TicketView.as_view(), name="ticket_view")
]
