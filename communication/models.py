from django.db import models
from django.contrib.auth.models import User
from lead.models import LeadProcess

MEDIUM_CHOICES = (
    ("Inbound Call", "Inbound Call"),
    ("Outbound Call", "Outbound Call"),
    ("Inbound Email", "Inbound Email"),
    ("Outbound Email", "Outbound Email"),
    ("Inbound Call", "Inbound Call"),
    ("Outbound Call", "Outbound Call"),
)

YES_NO = (
    ("Successful", "Successful"),
    ("Unsuccessful", "Unsuccessful")
)

class Clientlist(models.Model):
	
    client_name = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
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