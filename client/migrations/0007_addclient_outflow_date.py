# Generated by Django 2.0 on 2018-01-29 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_addclient_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='addclient',
            name='outflow_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
