# Generated by Django 2.1.2 on 2018-11-07 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_controller_number_of_t8000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controller',
            old_name='number_of_T8000',
            new_name='T8000s',
        ),
    ]
