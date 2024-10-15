from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import LoginUserForm

def login_user(request):
    error_message = ''

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('accounts:private_page_one')
            else:
                error_message = 'Invalid username or password. Try again.'
        else:
            error_message = 'Invalid username or password. Try again.'
    else:
        form = LoginUserForm()

    form = LoginUserForm()
    return render(request, 'accounts/login_user.html', {'form': form, 'error_message': error_message})

def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')

@login_required
def private_page_one(request):
    return render(request, 'accounts/private_page_one.html')

@login_required
def private_page_two(request):
    return render(request, 'accounts/private_page_two.html')