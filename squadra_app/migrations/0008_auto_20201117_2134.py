# Generated by Django 3.1.3 on 2020-11-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadra_app', '0007_auto_20201117_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='katalog',
            old_name='id_katalogu_nadrzednego',
            new_name='id_kat_nad',
        ),
        migrations.RenameField(
            model_name='pliki',
            old_name='format_pliku',
            new_name='format',
        ),
        migrations.RenameField(
            model_name='pliki',
            old_name='sciezka_do_plku',
            new_name='sciezka',
        ),
        migrations.AddField(
            model_name='pliki',
            name='nazwa',
            field=models.CharField(default='Nowy Plik', max_length=124),
        ),
    ]
