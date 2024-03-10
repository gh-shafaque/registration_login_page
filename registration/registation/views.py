from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


from .models import *

# Create your views here.
def registration(request):
    if request.method=='POST':
        email=request.POST["email"]
        name=request.POST["name"]
        phone_no=request.POST["phone_no"]
        password=request.POST["password"]
        if request.POST["password"]==request.POST["confirm_password"]:
            user=User.objects.create_user(email,password,name,phone_no)
            messages.success(request,'!You are registered')
            login(request, user)
            return redirect(dashboard)            
        else:
            messages.error(request, 'Both Password are not same!')
            return render(request,"registration.html",{"email":email,"name":name,"password":password,"phone_no":phone_no,"confirm_password":request.POST["confirm_password"]})
        
    return render(request,"registration.html")


# LOGIN PAGE
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            return redirect(dashboard)
    else:
        form = AuthenticationForm()

    return render(request, 'login_page.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html',{"name": request.user.name})

# logout page
def logout_page(request):
    # Perform any additional actions before logging out (if needed)
    # For example, you might want to log the user's logout activity

    # Logout the user
    logout(request)

    # Render the logout confirmation page
    return render(request, 'logout.html')