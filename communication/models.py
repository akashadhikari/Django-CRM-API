from django.db import models
from django.contrib.auth.models import User

from lead.models import LeadProcess
from client.models import AddClient
from common.utils import (

	MEDIUM_CHOICES,
	SALES_STAGE_CHOICES
	
	)

#################################################### COMMUNICATION MODEL ####################################################


class AddCommunication(models.Model):

	user = models.ForeignKey(User, related_name='user_addcommunication', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_addcommunication', on_delete=models.CASCADE)
	contact_person = models.CharField(max_length=255, blank=False)
	medium = models.CharField(max_length=255, choices=MEDIUM_CHOICES)
	sales_stage = models.CharField(max_length=255, choices=SALES_STAGE_CHOICES)

	def __str__(self):
		return "{}".format(self.client)

	def inbound_call(self):
		inbound_call_count = AddCommunication.objects.filter(medium='Inbound Call').count()
		return inbound_call_count

	def outbound_call(self):
		outbound_call_count = AddCommunication.objects.filter(medium='Outbound Call').count()
		return outbound_call_count

	def inbound_email(self):
		inbound_email_count = AddCommunication.objects.filter(medium='Inbound Email').count()
		return inbound_email_count

	def outbound_email(self):
		outbound_email_count = AddCommunication.objects.filter(medium='Outbound Email').count()
		return outbound_email_count

	def sms(self):
		sms_count = AddCommunication.objects.filter(medium='SMS').count()
		return sms_count

	def meeting(self):
		meeting_count = AddCommunication.objects.filter(medium='Meeting').count()
		return meeting_count


class Suspecting(models.Model):

	user = models.ForeignKey(User, related_name='user_suspecting', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_suspecting', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_suspecting', on_delete=models.CASCADE)
	contact_verification = models.CharField(max_length=255, blank=False)

class Prospecting(models.Model):

	user = models.ForeignKey(User, related_name='user_prospecting', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_prospecting', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_prospecting', on_delete=models.CASCADE)
	showed_interest_for_later = models.DateField()
	preferred_competitors = models.CharField(max_length=255, blank=False)
	not_interested = models.BooleanField(default=False)
	dont_call_again = models.BooleanField(default=False)
	interest_in_other_HR = models.BooleanField(default=False)
	remarks = models.TextField(max_length=999, blank=False)

class Approaching(models.Model):

	user = models.ForeignKey(User, related_name='user_approaching', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_approaching', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_approaching', on_delete=models.CASCADE)
	service_introduction = models.CharField(max_length=255, blank=False)
	business_renewal = models.CharField(max_length=255, blank=False)
	submit_proposal = models.CharField(max_length=255, blank=False)
	presentation = models.CharField(max_length=255, blank=False)

class Negotiation(models.Model):

	user = models.ForeignKey(User, related_name='user_negotiation', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_negotiation', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_negotiation', on_delete=models.CASCADE)
	service_discussion = models.CharField(max_length=255, blank=False)
	discount_discussion = models.CharField(max_length=255, blank=False)

class SalesLead(models.Model):

	user = models.ForeignKey(User, related_name='user_saleslead', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_saleslead', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_saleslead', on_delete=models.CASCADE)
	lead_generation = models.BooleanField(default=False)
	invoice_approval = models.CharField(max_length=255, blank=False)
	job_post = models.CharField(max_length=255, blank=False)
	pre_design = models.CharField(max_length=255, blank=False)
	approval_on_progress = models.CharField(max_length=255, blank=False)
	billing_process = models.CharField(max_length=255, blank=False)
	payment_on_progress = models.CharField(max_length=255, blank=False)
	payment_received = models.CharField(max_length=255, blank=False)
	payment_verified = models.CharField(max_length=255, blank=False)
