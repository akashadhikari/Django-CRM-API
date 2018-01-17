from django.db import models
from django.contrib.auth.models import User
from lead.models import LeadProcess
from common.utils import MEDIUM_CHOICES, YES_NO, SALES_STAGES

class ClientDetail(models.Model):
	
	client_name = models.CharField(max_length=255, blank=False)
	user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
	client_pic = models.ImageField(upload_to = 'common/files/images', default = 'common/files/images/display.png')
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	medium = models.CharField(max_length=255, choices=MEDIUM_CHOICES)
	medium_status = models.CharField(max_length=10, choices=YES_NO)
	contact_person = models.CharField(max_length=255, blank=False)
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