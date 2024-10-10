from django.shortcuts import render

def private_page_one(request):
    return render(request, 'accounts/private_page_one.html')

def private_page_two(request):
    return render(request, 'accounts/private_page_two.html')