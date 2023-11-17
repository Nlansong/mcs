from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ministry(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, blank=True)
    country = models.ForeignKey('cities_light.Country',on_delete=models.CASCADE)
    Region = models.ForeignKey('cities_light.Region',on_delete=models.CASCADE)
    Town = models.ForeignKey('cities_light.City',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='ministries', null=True, default="", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    
class Department(models.Model):
    options = [
        ('media','media'),
        ('choir','choir'),
        ('usering','ushering'),
        ('staff','staff'),
        ('follow-up','follow-up')
    ]
    
    name = models.CharField(max_length=155, choices=options)
    description = models.CharField(max_length=255)
    ministry = models.ForeignKey(Ministry, related_name='departments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'departments'
        
class Cell(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ministry = models.ForeignKey(Ministry, related_name='cells', on_delete=models.CASCADE)
    name_of_leader = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
        
#members
class Member(models.Model):
    options = [
        ('Brother','Brother'),
        ('Sister','Sister'),
        ('Pastor','Pastor'),
        ('Deacon','Deacon'),
        ('Deaconess','Deaconess'),
    ]
    
    g_options = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, choices=options, default="brother")
    gender = models.CharField(max_length=100, choices=g_options, default="male")
    active = models.BooleanField()
    added_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    ministry = models.ForeignKey(Ministry, related_name='ministry_members', on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, related_name='department_members', on_delete=models.CASCADE, null=True, blank=True)
    cell = models.ForeignKey(Cell, related_name='cell_members', on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255)
    picture= models.ImageField(upload_to='images/', null=True, blank=True)
    schooling = models.BooleanField()
    working = models.BooleanField()
    new_convert = models.BooleanField()
    pays_tithe = models.BooleanField()
    
   
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'members'