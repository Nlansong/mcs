from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ministry.models import Department, Ministry
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    if request.user.is_authenticated:
        profile = User.objects.get(pk=request.user.id)
        
        try:
            ministries = Ministry.objects.filter(created_by=request.user)
            #ministries = Ministry.objects.filter()
            departments = Department.objects.filter(created_by=request.user)
            
        except:
            departments =None
            ministries = None
        context = {
            'profile':profile,
            'departments':departments,
            'ministries':ministries,
        }
        return render(request, 'dashboard/index.html', context)
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('dasboard:index')
    
    
