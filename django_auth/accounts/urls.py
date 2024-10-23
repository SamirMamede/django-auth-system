from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', 
         auth_views.LoginView.as_view(), 
         name='login'),
    path('logout/', 
         auth_views.LogoutView.as_view(), 
         name='logout'),
    path('private_page_one/', 
         views.private_page_one, 
         name='private_page_one'),
    path('private_page_two/', 
         views.private_page_two, 
         name='private_page_two'),
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(success_url='/password_change_done/'), 
         name='password_change'),
    path('password_change_done/', 
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(success_url='/password_reset_done/'), 
         name='password_reset'),
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(), 
         name='password_reset_done'),
]