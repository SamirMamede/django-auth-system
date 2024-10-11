from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('private_page_one/', views.private_page_one, name='private_page_one'),
    path('private_page_two/', views.private_page_two, name='private_page_two'),
]