# Generated by Django 5.1.4 on 2024-12-10 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='comercio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_coder.comercio'),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='productos',
            field=models.ManyToManyField(to='app_coder.producto'),
        ),
    ]
