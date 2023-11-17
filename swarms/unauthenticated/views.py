from django.shortcuts import render
from django.views import View
# Create your views here.
class IndexPageView(View):
    def get(self, request):
        return render(request, "unauthenticated/unauthenticated.html")
    
class AboutUsPageView(View):
    def get(self, request):
        return render(request, "unauthenticated/about-us.html")

class LearnMoreHoneyBee(View):
    def get(self, request):
        return render(request, "unauthenticated/learn_more/honey-bee.html")