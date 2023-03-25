from django.views.generic import DetailView, CreateView, UpdateView
from django.shortcuts import render

from .forms import SignUpForm, ActivationForm
from .models import AuthorUser
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django import forms


class SignUp(CreateView):
    model = AuthorUser
    form_class = SignUpForm
    success_url = '/'
    template_name = 'registration/signup.html'

def Activation(request):
    submitbutton = request.POST.get("submit")

    email = ''
    code = ''
    form = ActivationForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        code = form.cleaned_data.get("code")
        # print(AuthorUser.objects.get(activation_code=code)
        if code == AuthorUser.objects.get(email=email).activation_code:
            AuthorUser.objects.filter(email=email).update(is_active = True)


    context = {'form': form, 'firstname': email,
               'lastname': code, 'submitbutton': submitbutton}

    return render(request, 'registration/activation.html', context)
#render(request, 'registration/activation.html', context)