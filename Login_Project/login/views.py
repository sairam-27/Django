from django.shortcuts import render
from login.forms import userForm,userProfileForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = userForm(data=request.POST)
        profile_form = userProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save( )

            registered = True
        
        else:
            print(user_form.errors,profile_form.errors)

    else:

        user_form = userForm()
        profile_form = userProfileForm()
    
    return render(request,'login/registration.html', {'registered': registered,
                                                       'userForm': user_form,
                                                       'userProfileForm': profile_form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login")
            print("Username: {} Password: {}".format(username,password))
            return HttpResponse('Invalid Response')
    else:
        return render(request,'login/login_page.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def test_login(request):
    return HttpResponse('Not logged in')
