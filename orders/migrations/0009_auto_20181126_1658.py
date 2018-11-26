# Generated by Django 2.1.3 on 2018-11-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20181107_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controller',
            name='controller_model',
        ),
        migrations.AlterField(
            model_name='controller',
            name='Buck_Converter_24v_to_12v',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='Buck_Converter_24v_to_5v',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='F16V3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='F2_Raspberry_Pi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='F4V3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='Raspberry_Pi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='T1000',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='T1000s',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='T4000',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='T8000',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='TP_Link',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='Three_Twenty_24_Volt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='controller',
            name='Two_Forty_24_Volt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
