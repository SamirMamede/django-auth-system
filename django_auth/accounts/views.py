from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import UserRegistrationForm, LoginUserForm

def home(request):
    return render(request, 'accounts/home.html')
@login_required
def private_page_one(request):
    return render(request, 'accounts/private_page_one.html')

@login_required
def private_page_two(request):
    return render(request, 'accounts/private_page_two.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})