# Generated by Django 2.0 on 2018-01-22 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('organisation_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('employee_size', models.CharField(choices=[('1-10', '1-10'), ('10-50', '10-50'), ('50-100', '50-100'), ('100-500', '100-500'), ('500+', '500+')], max_length=255)),
                ('client_value', models.CharField(choices=[('High', 'High'), ('Mid', 'Mid'), ('Low', 'Low')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan_no', models.CharField(max_length=255)),
                ('billing_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_incharge', models.CharField(max_length=255)),
                ('branch_address', models.CharField(max_length=255)),
                ('branch_phone', models.CharField(max_length=255)),
                ('branch_email', models.EmailField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_branch', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessOutflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outflowed_to', models.CharField(max_length=255)),
                ('service_outflowed', models.CharField(max_length=255)),
                ('outflow_date', models.DateField()),
                ('amount', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_businessoutflow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoreContactPersonDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('office_phone', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('social_media_id', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('mobile_no_head', models.IntegerField()),
                ('email_head', models.EmailField(max_length=100)),
                ('social_media_id_head', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ListService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('service_detail', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_listservice', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_website', models.CharField(max_length=255)),
                ('facebook_id', models.CharField(max_length=255)),
                ('linked_in_id', models.CharField(max_length=255)),
            ],
        ),
    ]
