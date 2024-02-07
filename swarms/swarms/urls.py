from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("unauthenticated.urls")),
    path("accounts/", include("allauth.urls")),
    path("report-a-swarm/", include("report_swarm.urls")),
    path("beekeeper/", include("sign_in_sign_out.urls")),
    path("beekeeper/tickets/", include("tickets.urls")),
]
