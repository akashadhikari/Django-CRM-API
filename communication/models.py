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
	contact_person = models.CharField(max_length=255, blank=False)
	medium = models.CharField(max_length=255, choices=MEDIUM_CHOICES)
	sales_stage = models.CharField(max_length=255, choices=SALES_STAGE_CHOICES)
