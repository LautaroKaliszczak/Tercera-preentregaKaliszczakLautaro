# Generated by Django 5.1.4 on 2024-12-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0003_alter_cliente_comercio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='productos',
            field=models.ManyToManyField(blank=True, null=True, to='app_coder.producto'),
        ),
    ]