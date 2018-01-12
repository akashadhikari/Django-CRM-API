from django.test import TestCase
from django.contrib.auth.models import User
from ..models import LeadProcess


class LeadProcessTest(TestCase):
    """ Test module for leadprocess model """

    def setUp(self):
        user = User.objects.create(username="nerd")
        LeadProcess.objects.create(
            service='Software', stage=3, status='Pending', bulk='True', user=user)
        LeadProcess.objects.create(
            service='Hardware', stage=1, status='Approved', bulk='True', user=user)

    def test_leadprocess_status(self):
        leadprocess_software = LeadProcess.objects.get(service='Software')
        leadprocess_hardware = LeadProcess.objects.get(service='Hardware')
        self.assertEqual(
            leadprocess_software.get_status(), "Software is in Pending status.")
        self.assertEqual(
            leadprocess_hardware.get_status(), "Hardware is in Approved status.")