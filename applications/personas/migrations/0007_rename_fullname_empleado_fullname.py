# Generated by Django 4.0.6 on 2022-08-14 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0006_empleado_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='fullname',
            new_name='fullName',
        ),
    ]