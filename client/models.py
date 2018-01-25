import datetime
from django.db import models
from django.contrib.auth.models import User

from common.utils import (
	EMPLOYEE_SIZE_CHOICES,
	CLIENT_VALUE_CHOICES,
	)

#################################################### SECONDARY INFORMATION ####################################################

class AddClient(models.Model):

	# NAME OF THE ORGANISATION

	user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
	client_name = models.CharField(max_length=255, blank=False)
	organisation_name = models.CharField(max_length=255, blank=False) 
	# MultipleChoiceField or django-multiselectfield
	#https://stackoverflow.com/questions/45153419/django-how-to-use-multiplechoicefield-in-a-form-admin
	address = models.CharField(max_length=255, blank=False)
	# phone_number = models.IntegerField(blank=False)
	# email_org = models.EmailField(max_length=100, blank=False)
	# introduction = models.TextField(max_length=999, blank=False)
	# ownership_type = models.CharField(max_length=255, blank=False)
	employee_size = models.CharField(max_length=255, choices=EMPLOYEE_SIZE_CHOICES)
	client_value  = models.CharField(max_length=15, choices=CLIENT_VALUE_CHOICES)
	created = models.DateField(auto_now=True)

	#logo = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')
	# attachments
	#client_pic = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')


	def __str__(self):
		return "{}".format(self.client_name)

	def today_created(self):
		# x = AddClient.objects.filter(created='2018-01-25')
		date_from = datetime.datetime.now() - datetime.timedelta(days=1)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

	def this_week_created(self):
		date_from = datetime.datetime.now() - datetime.timedelta(days=7)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

	def this_month_created(self):
		date_from = datetime.datetime.now() - datetime.timedelta(days=30)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

	def this_year_created(self):
		date_from = datetime.datetime.now() - datetime.timedelta(days=365)
		ctdays = AddClient.objects.filter(created__gte=date_from).count()
		return ctdays

class HeadOfOrganization(models.Model):

	# HEAD OF THE ORGANIZATION

	designation = models.CharField(max_length=255, blank=False)
	mobile_no_head = models.IntegerField(blank=False)
	email_head = models.EmailField(max_length=100, blank=False)
	social_media_id_head = models.CharField(max_length=255, blank=False)

class CoreContactPersonDetail(models.Model):

	#CORE CONTACT PERSON DETAIL

	client_name = models.CharField(max_length=255, blank=False)
	contact_person = models.CharField(max_length=255, blank=False)
	designation = models.CharField(max_length=255, blank=False)
	office_phone = models.IntegerField(blank=False)
	mobile_no = models.IntegerField(blank=False)
	email = models.EmailField(max_length=100, blank=False)
	social_media_id = models.CharField(max_length=255, blank=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

#################################################### SECONDARY INFORMATION ####################################################

class ReferenceClient(models.Model):

	#REFERENCE

	reference_website = models.CharField(max_length=255, blank=False)
	facebook_id = models.CharField(max_length=255, blank=False)
	linked_in_id = models.CharField(max_length=255, blank=False)

class BillingInfo(models.Model):

	# BILLING INFO

	pan_no = models.CharField(max_length=255, blank=False)
	billing_name = models.CharField(max_length=255, blank=False)

class BusinessOutflow(models.Model):

	# BUSINESS OUTFLOW

	user = models.ForeignKey(User, related_name='users_businessoutflow', on_delete=models.CASCADE)
	outflowed_to = models.CharField(max_length=255, blank=False)
	service_outflowed = models.CharField(max_length=255, blank=False)
	outflow_date = models.DateField(blank=False)
	amount = models.PositiveIntegerField(default=0)
	# attachment image


class ListService(models.Model):

	# LIST OF PRODUCT/SERVICES

	user = models.ForeignKey(User, related_name='users_listservice', on_delete=models.CASCADE)
	service_name = models.CharField(max_length=255, blank=False)
	service_detail = models.CharField(max_length=255, blank=False)
	# attachment image


class Branch(models.Model):

	# BRANCHES

	user = models.ForeignKey(User, related_name='users_branch', on_delete=models.CASCADE)
	branch_incharge = models.CharField(max_length=255, blank=False)
	branch_address = models.CharField(max_length=255, blank=False)
	branch_phone = models.CharField(max_length=255, blank=False)
	branch_email = models.EmailField(max_length=100, blank=False)