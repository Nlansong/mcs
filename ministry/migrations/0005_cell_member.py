# Generated by Django 4.2.4 on 2023-11-17 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ministry', '0004_alter_ministry_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('name_of_leader', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=255)),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='ministry.ministry')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[('Brother', 'Brother'), ('Sister', 'Sister'), ('Pastor', 'Pastor'), ('Deacon', 'Deacon'), ('Deaconess', 'Deaconess')], default='brother', max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='male', max_length=100)),
                ('active', models.BooleanField()),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('schooling', models.BooleanField()),
                ('working', models.BooleanField()),
                ('new_convert', models.BooleanField()),
                ('pays_tithe', models.BooleanField()),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cell_members', to='ministry.cell')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_members', to='ministry.department')),
                ('ministry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ministry_members', to='ministry.ministry')),
            ],
            options={
                'verbose_name_plural': 'members',
            },
        ),
    ]
