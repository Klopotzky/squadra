# Generated by Django 3.1.2 on 2020-11-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addProject', '0008_auto_20201114_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_user_cr', models.CharField(max_length=30)),
            ],
        ),
    ]
