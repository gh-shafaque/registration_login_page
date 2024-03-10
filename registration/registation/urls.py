from django.urls import path
from . import views

urlpatterns = [
    path("registration/",views.registration,name="registration"),
    path('login/', views.login_page, name='login_page'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_page, name='logout'),
]
