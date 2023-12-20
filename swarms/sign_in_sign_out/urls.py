from django.urls import path 
from . import views

urlpatterns = [
    path("profile", views.ProfileFormView.as_view(), name="profile"),
]
