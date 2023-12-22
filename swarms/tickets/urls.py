from django.urls import path 
from . import views
urlpatterns = [
    path("all", views.AllTicketView.as_view(), name="allTickets"),
    path("status/open", views.OpenTickets.as_view(), name="openTickets"),
]
