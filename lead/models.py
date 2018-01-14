from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

from common.utils import SERVICE_CHOICES, STATUSES


class LeadProcess(models.Model):

	user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE) 
	service = models.CharField(max_length=15, choices=SERVICE_CHOICES)
	status = models.CharField(max_length=15, choices=STATUSES)
	income = models.IntegerField(default=0)
	discount = models.IntegerField(default=0)
	tax_percent = models.PositiveIntegerField(default=1, 
		validators=[MinValueValidator(1), MaxValueValidator(25)])
	unit = models.PositiveIntegerField(default=1, 
		validators=[MinValueValidator(1)])
	bulk = models.BooleanField(default=False)
	stage = models.PositiveIntegerField(default=1, 
		validators=[MinValueValidator(1), MaxValueValidator(10)])
	created = models.DateTimeField(auto_now_add=True)

	### Some custom functions

	def username(self):
		return self.user.username

	def hardware_count(self):
		count_h = LeadProcess.objects.filter(service='Hardware').count()
		return count_h

	def software_count(self):
		count_s = LeadProcess.objects.filter(service='Software').count()
		return count_s

	def grand_total(self):
		return (self.income - self.discount + (self.tax_percent*self.income)/100)

	def get_status(self):
		return self.service + ' is in ' + self.status + ' status.'

	def __str__(self):
			return "{} at stage {}".format(self.service, self.stage)

	class Meta:
		ordering = ('-created',)
