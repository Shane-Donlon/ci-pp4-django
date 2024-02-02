from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .forms import ProfileForm
from .models import Profile


@method_decorator(login_required, name='dispatch')
class ProfileFormView(View):

    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(instance=request.user.profile)
        context = {"profile": profile,
                   "form": form}
        return render(request, "sign_in_sign_out/sign_in_sign_out.html", context)

    def post(self, request, *args, **kwargs):

        form = ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            # force another GET request after profile update
            return redirect("profile")
        else:

            context = {"form": form}
            return render(request, "sign_in_sign_out/sign_in_sign_out.html", context)
