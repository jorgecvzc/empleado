# Generated by Django 4.0.6 on 2022-07-20 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidades',
            old_name='hailidad',
            new_name='habilidad',
        ),
    ]