from django.urls import path

from . import views

urlpatterns = [
    # convert urls to snake_case and check all files
    path("", views.ReportSwarmView.as_view(), name="report_swarm"),
]
