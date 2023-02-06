from django.shortcuts import render

from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.urls import reverse_lazy
from django.views import generic

from django.http import HttpResponseRedirect, HttpResponseBadRequest

# class LogIn(generic.CreateView):
#     form_class = CustomAuthenticationForm
#     success_url = reverse_lazy('home')
#     template_name = 'login.html'

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('home')
#     template_name = 'signup.html'

from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            u = form.cleaned_data['username']
            p = form.cleaned_data['password1']
            new_user = authenticate(username = u, password = p)
            login(request, new_user)
            return HttpResponseRedirect("/dashboard/")
        else:
            # TODO more specific logic here
            return HttpResponseBadRequest('Something went wrong!')
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})
