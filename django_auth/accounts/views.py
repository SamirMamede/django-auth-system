from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def private_page_one(request):
    return render(request, 'accounts/private_page_one.html')

@login_required
def private_page_two(request):
    return render(request, 'accounts/private_page_two.html')