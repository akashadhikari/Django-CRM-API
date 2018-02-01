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
	address = models.CharField(max_length=255, blank=False)
	phone_number = models.IntegerField(blank=False)
	email_org = models.EmailField(max_length=100, blank=False)
	introduction = models.TextField(max_length=999, blank=False)
	ownership_type = models.CharField(max_length=255, blank=False)
	employee_size = models.CharField(max_length=255, choices=EMPLOYEE_SIZE_CHOICES)
	client_value  = models.CharField(max_length=15, choices=CLIENT_VALUE_CHOICES)
	created = models.DateField(auto_now=True)
	logo = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')

	# HEAD OF THE ORGANIZATION

	designation = models.CharField(max_length=255, blank=False)
	mobile_no_head = models.IntegerField(blank=False)
	email_head = models.EmailField(max_length=100, blank=False)
	social_media_id_head = models.CharField(max_length=255, blank=False)

	#CORE CONTACT PERSON DETAIL

	full_name = models.CharField(max_length=255, blank=False)
	designation_contactperson = models.CharField(max_length=255, blank=False)
	office_phone = models.IntegerField(blank=False)
	mobile_no = models.IntegerField(blank=False)
	email = models.EmailField(max_length=100, blank=False)
	social_media_id = models.CharField(max_length=255, blank=False)

#################################################### SECONDARY INFORMATION ####################################################

	#REFERENCE

	reference_website = models.CharField(max_length=255, blank=False)
	facebook_id = models.CharField(max_length=255, blank=False)
	linked_in_id = models.CharField(max_length=255, blank=False)

	# BILLING INFO

	pan_no = models.CharField(max_length=255, blank=False)
	billing_name = models.CharField(max_length=255, blank=False)

	# BUSINESS OUTFLOW -- SHOULD BE MULTIPLE

	outflowed_to = models.CharField(max_length=255, blank=False)
	service_outflowed = models.CharField(max_length=255, blank=False)
	outflow_date = models.DateField(auto_now_add=True)
	amount = models.PositiveIntegerField(default=0)

	# BRANCHES

	branch_incharge = models.CharField(max_length=255, blank=False)
	branch_address = models.CharField(max_length=255, blank=False)
	branch_phone = models.CharField(max_length=255, blank=False)
	branch_email = models.EmailField(max_length=100, blank=False)


	def __str__(self):
		return "{}".format(self.client_name)
		

class ListOfProduct(models.Model):

	# LIST OF PRODUCT/SERVICES

	user = models.ForeignKey(User, related_name='users_listofproduct', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_listofproduct', on_delete=models.CASCADE)

	service_name = models.CharField(max_length=255, blank=False)
	service_detail = models.CharField(max_length=255, blank=False)

	def user_name(self):
		return self.user.username

	def client_name(self):
		return self.client.client_name

	def __str__(self):
		return "{}".format(self.service_name)