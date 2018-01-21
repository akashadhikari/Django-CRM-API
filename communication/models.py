from django.db import models
from django.contrib.auth.models import User

from lead.models import LeadProcess
from common.utils import (
	EMPLOYEE_SIZE_CHOICES,
	CLIENT_VALUE_CHOICES,
	YES_NO,
	SALES_STAGES
	)

# BRANCHES

class Branch(models.Model):
	user = models.ForeignKey(User, related_name='users_branch', on_delete=models.CASCADE)
	branch_incharge = models.CharField(max_length=255, blank=False)
	branch_address = models.CharField(max_length=255, blank=False)
	branch_phone = models.CharField(max_length=255, blank=False)
	branch_email = models.EmailField(max_length=100, blank=False)

# BUSINESS OUTFLOW

class BusinessOutflow(models.Model):
	user = models.ForeignKey(User, related_name='users_businessoutflow', on_delete=models.CASCADE)
	outflowed_to = models.CharField(max_length=255, blank=False)
	service_outflowed = models.CharField(max_length=255, blank=False)
	outflow_date = models.DateField(blank=False)
	amount = models.PositiveIntegerField(default=0)
	# attachment image

# LIST OF PRODUCT/SERVICES

class ListService(models.Model):
	user = models.ForeignKey(User, related_name='users_listservice', on_delete=models.CASCADE)
	service_name = models.CharField(max_length=255, blank=False)
	service_detail = models.CharField(max_length=255, blank=False)
	# attachment image

class ClientDetail(models.Model):

	user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
	client_name = models.CharField(max_length=255, blank=False)

	# NAME OF ThE ORGANISATION

	group_of_companies = models.BooleanField(default=False)
	organisation_name = models.CharField(max_length=255, blank=False) 
	# MultipleChoiceField or django-multiselectfield
	#https://stackoverflow.com/questions/45153419/django-how-to-use-multiplechoicefield-in-a-form-admin
	address = models.CharField(max_length=255, blank=False)
	phone_number = models.IntegerField(blank=False)
	email_org = models.EmailField(max_length=100, blank=False)
	introduction = models.TextField(max_length=999, blank=False)
	ownership_type = models.CharField(max_length=255, blank=False)
	employee_size = models.CharField(max_length=255, choices=EMPLOYEE_SIZE_CHOICES)
	#logo = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')
	# attachments
	client_value  = models.CharField(max_length=15, choices=CLIENT_VALUE_CHOICES)
	client_pic = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')

	# HEAD OF THE ORGANIZATION

	designation = models.CharField(max_length=255, blank=False)
	mobile_no_head = models.IntegerField(blank=False)
	email_head = email = models.EmailField(max_length=100, blank=False)
	social_media_id_head = models.CharField(max_length=255, blank=False)

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

	#REFERENCE

	reference_website = models.CharField(max_length=255, blank=False)
	facebook_id = models.CharField(max_length=255, blank=False)
	linked_in_id = models.CharField(max_length=255, blank=False)

	# BILLING INFO

	pan_no = models.CharField(max_length=255, blank=False)
	billing_name = models.CharField(max_length=255, blank=False)

	# ADDITIONAL

	remarks = models.TextField(max_length=999, blank=False)
	lead = models.ForeignKey(LeadProcess, related_name='lead', on_delete=models.CASCADE)

	def get_contact_person(self):
		return self.client_name + ' is in touch with ' + self.contact_person

	def __str__(self):
		return "{}".format(self.client_name)


class SalesStage(models.Model):
	substage = models.CharField(max_length=100)
	sales_stage = models.CharField(max_length=100, choices=SALES_STAGES)
	client = models.ForeignKey(ClientDetail, related_name='client_sales', on_delete=models.DO_NOTHING)
	user = models.ForeignKey(User, related_name='users_salesstage', on_delete=models.CASCADE)

	def get_substage(self):
		return self.substage + ' falls under ' + self.sales_stage

	def __str__(self):
		return "{}-{}".format(self.sales_stage, self.substage)

class SalesSub(models.Model):
	sales_substage = models.CharField(max_length=100, blank=False)
	substage = models.ForeignKey(SalesStage, related_name='sub_stage', on_delete=models.DO_NOTHING)
	client = models.ForeignKey(ClientDetail, related_name='client_salessub', on_delete=models.DO_NOTHING)
	user = models.ForeignKey(User, related_name='users_salessub', on_delete=models.CASCADE)

	def get_salessubstage(self):
		return self.substage.sales_stage + ' childrens to ' + self.sales_substage

	def __str__(self):
		return "{}".format(self.sales_substage)

	def inbound_call(self):
		inbound = ClientDetail.objects.filter(medium='Inbound Call').count()
		return inbound
		
	def outbound_call(self):
		outbound = ClientDetail.objects.filter(medium='Outbound Call').count()
		return outbound