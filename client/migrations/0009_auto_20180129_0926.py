# Generated by Django 2.0 on 2018-01-29 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0008_auto_20180129_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('service_detail', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='businessoutflow',
            name='client',
        ),
        migrations.RemoveField(
            model_name='businessoutflow',
            name='user',
        ),
        migrations.RenameField(
            model_name='addclient',
            old_name='service_detail',
            new_name='outflowed_to',
        ),
        migrations.RenameField(
            model_name='addclient',
            old_name='service_name',
            new_name='service_outflowed',
        ),
        migrations.AddField(
            model_name='addclient',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addclient',
            name='outflow_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BusinessOutflow',
        ),
        migrations.AddField(
            model_name='listofproduct',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_listofproduct', to='client.AddClient'),
        ),
        migrations.AddField(
            model_name='listofproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_listofproduct', to=settings.AUTH_USER_MODEL),
        ),
    ]
