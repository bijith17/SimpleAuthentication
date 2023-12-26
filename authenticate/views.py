from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
from authenticate.registerForm import userRegForm
from django.contrib.auth.hashers import make_password,check_password
from django.core.exceptions import ObjectDoesNotExist


def RegisterPage(request):
    regForm = userRegForm()    
    if request.method == 'POST': 
        regForm = userRegForm(request.POST)    
        if regForm.is_valid():
            password=regForm.cleaned_data['password']
            newPassword=make_password(password)
            regForm.instance.password =newPassword
            regForm.save()
            messages.success(request,'Data inserted Successfully')
        else:
            print(regForm.errors)
    else:
        regForm=userRegForm()
    return render(request,'register.html',{'formValue': regForm})


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            checkUser = RegisterData.objects.get(name=username,)
            name=checkUser.name
        except ObjectDoesNotExist:
            # Handle the case where the user with the specified username doesn't exist
            return redirect('reg')

        if check_password(password, checkUser.password):
            request.session['aUser'] = checkUser.name
            return render(request,'home.html',{'username':name})
        else:
            # Handle the case where the password doesn't match
            return redirect('reg')

    return render(request, 'login.html')


def HomePage(request):
    userSession= request.session.get('aUser')
    if userSession:
            return render(request,'home.html')
    else:
        return redirect('login')
        
def Logout(request):
    request.session.clear()
    return redirect('login')

