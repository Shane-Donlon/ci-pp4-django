from django.shortcuts import render,get_object_or_404
from .forms import ProfileForm
from django.views import View
from django.contrib.auth.models import User
from .models import Profile

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class ProfileFormView(View):
    
    def get(self, request):

        profile = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(instance=request.user)
 
        context = {"profile": profile,
                   "form":form}
        return render(request, "sign_in_sign_out/sign_in_sign_out.html", context)
    
    def post(self, request,*args, **kwargs):
       
        form = ProfileForm(request.POST,instance=request.user.profile) 

        if form.is_valid():
            form.save()
            print("form saved")
            return render(request, "sign_in_sign_out/sign_in_sign_out.html",)
        else:
            print("form not valid")
            context = {"form":form}
            return render(request, "sign_in_sign_out/sign_in_sign_out.html",context)
