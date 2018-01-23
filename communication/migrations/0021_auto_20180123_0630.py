# Generated by Django 2.0 on 2018-01-23 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communication', '0020_prospecting_communication'),
    ]

    operations = [
        migrations.AddField(
            model_name='approaching',
            name='communication',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='communication_approaching', to='communication.AddCommunication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='approaching',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_approaching', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negotiation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_negotiation', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saleslead',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_saleslead', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
