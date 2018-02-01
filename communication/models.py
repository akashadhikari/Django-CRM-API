from django.db import models
from django.contrib.auth.models import User

from lead.models import LeadProcess
from client.models import AddClient
from common.utils import (

	MEDIUM_CHOICES,
	SALES_STAGE_CHOICES,
	MEDIUM_DIRECTION_CHOICES,

	SUSPECTING_CHOICES,
	PROSPECTING_CHOICES,
	APPROACHING_CHOICES,
	NEGOTIATION_CHOICES,
	
	)

#################################################### COMMUNICATION MODEL ####################################################


class AddCommunication(models.Model):

	user = models.ForeignKey(User, related_name='user_addcommunication', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_addcommunication', on_delete=models.CASCADE)
	contact_person = models.CharField(max_length=255, blank=False)
	medium = models.CharField(max_length=255, choices=MEDIUM_CHOICES)
	medium_direction = models.CharField(max_length=255, choices=MEDIUM_DIRECTION_CHOICES)
	medium_status = models.BooleanField(default=True)
	sales_stage = models.CharField(max_length=255, choices=SALES_STAGE_CHOICES)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}".format(self.client)

	def user_name(self):
		return self.user.username

	def client_name(self):
		return self.client.client_name


class Suspecting(models.Model):

	user = models.ForeignKey(User, related_name='user_suspecting', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_suspecting', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_suspecting', on_delete=models.CASCADE)

	suspecting_substages = models.CharField(max_length=255, choices=SUSPECTING_CHOICES)

	def __str__(self):
		return "{}".format(self.client)

class Prospecting(models.Model):

	user = models.ForeignKey(User, related_name='user_prospecting', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_prospecting', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_prospecting', on_delete=models.CASCADE)

	prospecting_substages = models.CharField(max_length=255, choices=PROSPECTING_CHOICES)

	def __str__(self):
		return "{}".format(self.client)

class Approaching(models.Model):

	user = models.ForeignKey(User, related_name='user_approaching', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_approaching', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_approaching', on_delete=models.CASCADE)

	approaching_substages = models.CharField(max_length=255, choices=APPROACHING_CHOICES)

	def __str__(self):
		return "{}".format(self.client)

class Negotiation(models.Model):

	user = models.ForeignKey(User, related_name='user_negotiation', on_delete=models.CASCADE)
	client = models.ForeignKey(AddClient, related_name='client_negotiation', on_delete=models.CASCADE)
	communication = models.ForeignKey(AddCommunication, related_name='communication_negotiation', on_delete=models.CASCADE)

	negotiation_substages = models.CharField(max_length=255, choices=NEGOTIATION_CHOICES)

	def __str__(self):
		return "{}".format(self.client)
