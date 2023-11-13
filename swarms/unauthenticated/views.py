from django.shortcuts import render

# Create your views here.
def testingView(request):
    return render(request, "unauthenticated/unauthenticated.html")