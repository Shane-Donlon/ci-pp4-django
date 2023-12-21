from django.urls import path 
from . import views
urlpatterns = [
    path("all", views.SuperUserView.as_view(), name="allTickets"),
]
