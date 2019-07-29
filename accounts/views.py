from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'A User With This Username Exists')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'A User With This Email Already Exists')
                    return redirect('register')

                else:
                    #Looks Good

                    user = User.objects.create_user(username=username, password=password,
                                                    email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Successfully Registered')
                    return redirect('login')
        else:
            messages.error(request, 'Password Do not Match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('dashboard')

        else:
            messages.error(request, 'Incorrect Username Or Password Try Again or Sign Up')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You Are Logged Out')
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
