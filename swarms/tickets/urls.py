from django.urls import path 
from . import views
urlpatterns = [
    path("all", views.AllTicketView.as_view(), name="allTickets"),
    path("status/open", views.OpenTickets.as_view(), name="openTickets"),
    path("status/resolved", views.ResolvedTickets.as_view(), name="resolvedTickets"),
    path("status/closed-not-solved", views.UnResolvedClosedTickets.as_view(), name="resolvedTickets"),
    path("<int:ticketID>",views.TicketView.as_view(), name="ticketView")
]
