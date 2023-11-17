from django.contrib import admin
from .models import Ministry, Department, Cell, Member

# Register your models here.
admin.site.register(Ministry)
admin.site.register(Department)
admin.site.register(Cell)
admin.site.register(Member)
