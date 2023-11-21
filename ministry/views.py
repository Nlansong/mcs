from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Ministry, Department, Member, Cell

# Create your views here.
#url for this view can be found in the dashboard urls list
@login_required
def church_profile(request):
    ministry = Ministry.objects.get(created_by=request.user)
    all_members = Member.objects.filter(ministry=ministry).count()
    total_male = Member.objects.filter(ministry=ministry, gender='Male').count()
    total_female = Member.objects.filter(ministry=ministry, gender='Female').count()
    
    #active members of the ministry
    total_active = Member.objects.filter(ministry=ministry, active=True).count()
    total_active_male = Member.objects.filter(ministry=ministry, active=True, gender="Male").count()
    total_active_female = Member.objects.filter(ministry=ministry, active=True, gender="Female").count()
    
    #working Members of the ministry
    total_working_members = Member.objects.filter(ministry=ministry, working=True).count()
    total_working_male = Member.objects.filter(ministry=ministry, gender="Male").count()
    total_working_female = Member.objects.filter(ministry=ministry, gender="Female").count()
    
    #Student Members of the ministry
    total_students =Member.objects.filter(ministry=ministry, schooling=True).count()
    total_male_students = Member.objects.filter(ministry=ministry, schooling=True, gender='Male').count()
    total_female_students = Member.objects.filter(ministry=ministry, schooling=True, gender='Female').count()
    
    #number of new Converts in the Ministry
    total_converts = Member.objects.filter(ministry=ministry, new_convert=True).count()
    total_male_converts = Member.objects.filter(ministry=ministry, new_convert=True, gender='Male').count()
    total_female_converts = Member.objects.filter(ministry=ministry, new_convert=True, gender='Female').count()
    context = {
        'ministry':ministry,
        'all_members':all_members,
        'total_male':total_male,
        'total_female':total_female,
        'total_working_members':total_working_members,
        'total_working_male':total_working_male,
        'total_working_female':total_working_female,
        'total_active':total_active,
        'total_active_male':total_active_male,
        'total_active_female':total_active_female,
        'total_students':total_students,
        'total_male_students':total_male_students,
        'total_female_students':total_female_students,
        'total_converts':total_converts,
        'total_male_converts':total_male_converts,
        'total_female_converts':total_female_converts,
        
    }
    
    return render(request, 'ministry/church-profile.html', context)

#list all departments in the ministry
@login_required
def department_list(request):
    ministry = Ministry.objects.get(created_by=request.user)
    departments = Department.objects.filter(ministry=ministry)
    context = {
        'ministry':ministry,
        'departments':departments
    }
    
    return render(request, 'ministry/departments.html', context)


# members of department detail page
@login_required
def dep_detail(request, pk):
    ministry = Ministry.objects.get(created_by=request.user)
    department = get_object_or_404(Department, pk=pk, ministry=ministry)
    members = Member.objects.filter(department=department)
    context = {
        'ministry':ministry,
        'department':department,
        'members':members
    }
    
    return render(request, 'ministry/dep-detail.html', context)


#List of cells
@login_required
def cell_list(request):
    ministry = Ministry.objects.get(created_by = request.user)
    cells = Cell.objects.filter(ministry=ministry)
    context = {
        'ministry':ministry,
        'cells':cells,
    }
    
    return render(request, 'ministry/cells.html', context)


#list of members by cell
@login_required
def cell_detail(request, pk):
    ministry = Ministry.objects.get(created_by=request.user)
    cell = get_object_or_404(Cell, pk=pk, ministry=ministry)
    members = Member.objects.filter(cell=cell)
    context = {
        'ministry':ministry,
        'cell':cell,
        'members':members
    }
    
    return render(request, 'ministry/cell-detail.html', context)


# list of members of the ministry
@login_required
def members_list(request):
    ministry = Ministry.objects.get(created_by=request.user)
    members = Member.objects.filter(ministry=ministry)[0:10]
    
    #set the number of members per page
    # members_per_page = 10
    # paginator = Paginator(members,members_per_page )
    
    # #get the current page
    # page = request.GET.get('page')
    # try:
    #     page_members = paginator.page(page)
    # except PageNotAnInteger:
    #     page_members =  paginator.page(1)
    # except EmptyPage:
    #     page_members = paginator.page(paginator.num_pages)
    
    context = {
        'ministry':ministry,
        'members':members
    }
    
    return render(request, 'ministry/members.html', context)

# detail member view
@login_required
def mem_detail(request, pk):
    ministry = Ministry.objects.get(created_by=request.user)
    member = get_object_or_404(Member, pk=pk, ministry=ministry)
    
    context = {
        'ministry':ministry,
        'member':member,
    }
    
    return render(request, 'ministry/mem-detail.html', context)


#active members
@login_required
def active_members(request):
    ministry = Ministry.objects.get(created_by=request.user)
    members =Member.objects.filter(ministry=ministry, active=True)[0:10]
    
    context = {
        'ministry':ministry,
        'members':members
    }
    
    return render(request, 'ministry/active-members.html', context)

#list of working members
@login_required
def working_members(request):
    ministry = Ministry.objects.get(created_by=request.user)
    members =Member.objects.filter(ministry=ministry, working=True)[0:10]
    
    context = {
        'ministry':ministry,
        'members':members,
    }
    
    return render(request, 'ministry/working-members.html', context)

# schooling Members of the ministry
@login_required
def student_members(request):
    ministry = Ministry.objects.get(created_by=request.user)
    members =Member.objects.filter(ministry=ministry, schooling=True)[0:10]
    
    context = {
        'ministry':ministry,
        'members':members,
    }
    
    return render(request, 'ministry/student-members.html', context)

#list of new converts
@login_required
def new_converts(request):
    ministry = Ministry.objects.get(created_by=request.user)
    members =Member.objects.filter(ministry=ministry, new_convert=True)[0:10]
    
    context = {
        'ministry':ministry,
        'members':members,
    }
    
    return render(request, 'ministry/new-convert.html', context)

#list of members by Gender
@login_required
def male_members(request):
    ministry = Ministry.objects.get(created_by=request.user)
    members =Member.objects.filter(ministry=ministry, gender='Male')[0:10]
    
    
    context = {
        'ministry':ministry,
        'members':members,
    }
    
    return render(request, 'ministry/male-members.html', context)