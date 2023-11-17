from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm

# Create your views here.
def index(request):
    form = LoginForm()
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
    else:
        form = LoginForm()
    return render(request, 'auth_app/index.html', {'form':form})


def signup_user(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()
    context = {
        'form':form
    }
    return render(request, 'auth_app/signup.html', context)



#logou user
def logout_user(request):
    logout(request)
    return redirect('/')
