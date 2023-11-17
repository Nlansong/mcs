from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ministry, Department
# Create your views here.
#url for this view can be found in the dashboard urls list
@login_required
def church_profile(request):
    churches = Ministry.objects.all()
    context = {
        'churches':churches,
    }
    
    return render(request, 'ministry/church-profile.html', context)
