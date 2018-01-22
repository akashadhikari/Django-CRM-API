# Generated by Django 2.0 on 2018-01-22 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead', '0003_auto_20180117_0717'),
        ('communication', '0005_auto_20180121_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan_no', models.CharField(max_length=255)),
                ('billing_name', models.CharField(max_length=255)),
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
            name='NameOfOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('group_of_companies', models.BooleanField(default=False)),
                ('organisation_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('email_org', models.EmailField(max_length=100)),
                ('introduction', models.TextField(max_length=999)),
                ('ownership_type', models.CharField(max_length=255)),
                ('employee_size', models.CharField(choices=[('1-10', '1-10'), ('10-50', '10-50'), ('50-100', '50-100'), ('100-500', '100-500'), ('500+', '500+')], max_length=255)),
                ('client_value', models.CharField(choices=[('High', 'High'), ('Mid', 'Mid'), ('Low', 'Low')], max_length=15)),
                ('client_pic', models.ImageField(default='common/files/images/display.png', upload_to='common/files/images')),
                ('remarks', models.TextField(max_length=999)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead', to='lead.LeadProcess')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
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
        migrations.RemoveField(
            model_name='clientdetail',
            name='lead',
        ),
        migrations.RemoveField(
            model_name='clientdetail',
            name='user',
        ),
        migrations.RemoveField(
            model_name='salesstage',
            name='client',
        ),
        migrations.RemoveField(
            model_name='salesstage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='salessub',
            name='client',
        ),
        migrations.RemoveField(
            model_name='salessub',
            name='substage',
        ),
        migrations.RemoveField(
            model_name='salessub',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClientDetail',
        ),
        migrations.DeleteModel(
            name='SalesStage',
        ),
        migrations.DeleteModel(
            name='SalesSub',
        ),
    ]