# Generated by Django 4.2.4 on 2023-11-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0005_cell_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]
