from django.urls import path 
from . import views

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="home"),
    path("about-us", views.AboutUsPageView.as_view(), name="about"),
    path("learn-more/honeybee", views.LearnMoreHoneyBee.as_view(), name="learnhoneybee"),
]
