# Generated by Django 3.1.3 on 2020-11-17 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('squadra_app', '0008_auto_20201117_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='id_kat_nad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='squadra_app.katalog'),
        ),
    ]
