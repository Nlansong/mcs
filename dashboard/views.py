from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ministry.models import Department, Ministry, Cell, Member
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        
        
        try:
            ministries = Ministry.objects.filter(created_by=request.user)
            ministry = Ministry.objects.get(created_by=request.user)
            departments = Department.objects.filter(ministry=ministry)
            total_departments = Department.objects.filter(ministry=ministry).count()
            total_cells = Cell.objects.filter(ministry=ministry).count()
            
        except:
            departments =None
            ministries = None
        context = {
            'departments':departments,
            'ministries':ministries,
            'total_departments':total_departments,
            'ministry':ministry,
            'total_cells':total_cells,
        }
        return render(request, 'dashboard/index.html', context)
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('dasboard:index')
    
    

# list of members of the ministry
@login_required
def list_members(request):
    ministry = Ministry.objects.get(created_by=request.user)
    members = Member.objects.filter(ministry=ministry)
    total_members = Member.objects.filter(ministry=ministry).count()
    context = {
        'ministry':ministry,
        'members':members,
        'total_members': total_members,
    }
    return render(request, 'dashboard/members.html', context)