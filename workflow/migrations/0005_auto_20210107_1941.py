# Generated by Django 3.1.4 on 2021-01-07 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_auto_20210107_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='prioryty',
            new_name='priority',
        ),
    ]
