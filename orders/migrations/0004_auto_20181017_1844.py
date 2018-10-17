# Generated by Django 2.1.2 on 2018-10-17 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181016_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_first_name',
            new_name='customer_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='ride',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.Ride'),
        ),
    ]