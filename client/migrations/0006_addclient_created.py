# Generated by Django 2.0 on 2018-01-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20180129_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='addclient',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]