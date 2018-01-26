from django.db import models
from django.contrib.auth.models import User

from client.models import AddClient
from common.utils import (
	CLIENT_VALUE_CHOICES,
	SERVICE_TYPE_CHOICES,
	STAGES_CHOICES,
	DISCOUNT_ENTRY_CHOICES,
	LAST_STATUS_CHOICES
)


class LeadProcess(models.Model):

	user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
	employer_name = models.CharField(max_length=255, blank=False)

	# :::CLIENT BASIC INFO:::
	client = models.ForeignKey(AddClient, related_name='client_lead', on_delete=models.CASCADE)
	client_value  = models.CharField(max_length=15, choices=CLIENT_VALUE_CHOICES)
	client_address = models.CharField(max_length=255, blank=False)
	contact_person = models.CharField(max_length=255, blank=False)
	pan_no = models.CharField(max_length=255, blank=False)
	billing_name = models.CharField(max_length=255, blank=False)

	service_type = models.CharField(max_length=15, choices=SERVICE_TYPE_CHOICES)
	bulk = models.BooleanField(default=False)
	stages = models.CharField(max_length=15, choices=STAGES_CHOICES)


	# :::AMOUNT CALCULATION:::

	amount = models.IntegerField(default=0) # amount
	discount_entry = models.CharField(max_length=255, choices=DISCOUNT_ENTRY_CHOICES)
	discount = models.IntegerField(default=0) # flat or percentage
	vat_percent = models.PositiveIntegerField(default=13)

	# :::DISPLAY CLIENT'S BASIC BEHAVIOUR:::

	last_communicated = models.DateField(auto_now=True)
	last_status = models.CharField(max_length=15, choices=LAST_STATUS_CHOICES)
	last_service_taken = models.DateField(auto_now=True)
	last_service_name = models.CharField(max_length=255, blank=False)
	# last_payment_status -- define a function that subtracts invoice date to payment date interval
	# value proposition ??

	created = models.DateTimeField(auto_now_add=True)

	### Some custom methods ###

	def total_amount(self):
		if(self.discount_entry=='Percentage'):
			return (self.amount - self.discount*self.amount/100)
		elif(self.discount_entry=='Flat'):
			return (self.amount - self.discount)

	def total_invoicing_amount(self):
		return (self.total_amount() + self.vat_percent*self.total_amount()/100)

	def username(self): # defined for serializer
		return self.user.username

	def top_job(self):
		count_tj = LeadProcess.objects.filter(service_type='Hardware').count()
		return count_tj

	def hot_job(self):
		count_hj = LeadProcess.objects.filter(service_type='Software').count()
		return count_hj

	def f_post(self):
		count_fp = LeadProcess.objects.filter(service_type='Hardware').count()
		return count_fp

	def g_post(self):
		count_gp = LeadProcess.objects.filter(service_type='Software').count()
		return count_gp

	def get_billing_name(self):
		return self.post_type + ' has billing name ' + self.billing_name

	def __str__(self):
		return "{} by {}".format(self.service_type, self.billing_name)

	class Meta:
		ordering = ('-created',)
