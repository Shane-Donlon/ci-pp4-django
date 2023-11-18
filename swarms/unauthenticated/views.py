from django.shortcuts import render
from django.views import View
from .models import Faq
# Create your views here.
class IndexPageView(View):
    
    def get(self, request):
        context = {"faq": Faq.objects.filter(status="Shown")}
        return render(request, "unauthenticated/unauthenticated.html", context)
    
class AboutUsPageView(View):
    def get(self, request):
        return render(request, "unauthenticated/about-us.html")

