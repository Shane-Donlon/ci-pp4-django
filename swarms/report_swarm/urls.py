from django.urls import path

from . import views

urlpatterns = [
     path("", views.ReportSwarmView.as_view(), name="report_swarm"),
]
