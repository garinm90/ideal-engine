# Generated by Django 2.1.3 on 2018-11-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_controllerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]