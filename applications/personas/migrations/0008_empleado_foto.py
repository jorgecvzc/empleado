# Generated by Django 4.0.6 on 2022-08-14 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_rename_fullname_empleado_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
