# Generated by Django 2.2.11 on 2020-05-07 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200507_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patologia',
            old_name='nombre',
            new_name='nombrepatologia',
        ),
        migrations.RenameField(
            model_name='sistema',
            old_name='nombre',
            new_name='nombresistema',
        ),
    ]
