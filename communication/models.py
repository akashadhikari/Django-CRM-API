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

class Suspecting(models.Model):

	user = models.ForeignKey(User, related_name='user_suspecting', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_suspecting', on_delete=models.CASCADE)
	communications = models.ForeignKey(AddCommunication, related_name='add_comunications', on_delete=models.CASCADE)
	contact_verification = models.CharField(max_length=255, blank=False)

class Prospecting(models.Model):

	user = models.ForeignKey(User, related_name='user_prospecting', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_prospecting', on_delete=models.CASCADE)
	showed_interest_for_later = models.DateField()
	preferred_competitors = models.CharField(max_length=255, blank=False)
	not_interested = models.BooleanField(default=False)
	dont_call_again = models.BooleanField(default=False)
	interest_in_other_HR = models.BooleanField(default=False)
	remarks = models.TextField(max_length=999, blank=False)
