from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('account:login')
    else:
        user_form = UserCreationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# class MyLoginView(LoginView):
#     template_name = 'account/login.html'
#     model = CustomAuthenticationForm