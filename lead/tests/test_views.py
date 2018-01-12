import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import LeadProcess
from ..serializers import LeadProcessSerializer


# initialize the APIClient app
client = Client()