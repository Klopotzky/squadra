# Generated by Django 3.1.3 on 2020-11-17 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0006_katalog_nazwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='id_katalogu_nadrzednego',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='editor.katalog'),
        ),
    ]