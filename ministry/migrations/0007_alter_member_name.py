# Generated by Django 4.2.4 on 2023-11-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0006_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
