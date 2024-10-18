from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import LoginUserForm

@login_required
def private_page_one(request):
    return render(request, 'accounts/private_page_one.html')

@login_required
def private_page_two(request):
    return render(request, 'accounts/private_page_two.html')