# Generated by Django 4.2.4 on 2023-11-19 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0007_alter_member_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='slug',
        ),
    ]
