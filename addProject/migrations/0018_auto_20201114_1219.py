# Generated by Django 3.1.2 on 2020-11-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addProject', '0017_auto_20201114_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_project',
            name='project_name',
            field=models.CharField(max_length=30),
        ),
    ]
