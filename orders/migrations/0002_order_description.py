# Generated by Django 2.1.2 on 2018-10-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
