from django.shortcuts import render, redirect
from login_signup.forms import CreateClientForm, CreateAdminForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, client_required
from django.contrib.auth import authenticate, login,logout  
import requests
import sweetify
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.encoding import force_bytes
from .models import User

# Create your views here.


def clientregisterPage(request):

    if request.method == 'POST':
        form = CreateClientForm(request.POST)

        if form.is_valid():    

            user = form.save()                                                              
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('login_signup/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)  
            sweetify.success(request, 'Account Successfully Registered!', text='Please ! Check your email address to activate account.', persistent='Ok', icon='success')
            return redirect('login')   

        else:

            context = {'form': form}
            return render(request, 'login_signup/register.html', context)

    else:
        form = CreateClientForm()
        context = {'form': form}
        return render(request, 'login_signup/register.html', context)



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_verified = True
        user.save()

        sweetify.success(request, 'Account Activated Successfully!',
                         text='Please! Login with your credentials', persistent='Ok', icon='success')
        return redirect('login')
    else:
        return render(request, 'login_signup/activation_invalid.html')



@login_required
@admin_required
def adminregisterPage(request):
    form = CreateAdminForm()

    if request.method == 'POST':
        form = CreateAdminForm(request.POST)

        if form.is_valid():
            user = form.save()  
            username = form.cleaned_data.get('username')  
            messages.success(request, username + ' is also added as a new Admin.')  
            return redirect('adminhome')  

    context = {'form': form}
    return render(request, 'login_signup/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:  
            login(request,user)  
            if request.user.is_client:
                return redirect('clienthome')
            else:
                return redirect('adminhome')
        else:
            messages.error(request,'Username OR password is incorrect') 

    context = {}
    if not request.user.is_authenticated:
        return render(request, 'login_signup/login.html', context)
    else:
        return redirect('home')



@login_required
def logoutall(request, reason=''):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('home')
