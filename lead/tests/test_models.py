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

    def test_get_lead_object_with_status(self):
        lead_process = LeadProcess.objects.get(service="Hardware")
        self.assertEqual(lead_process.status, "Approved")

    def test_service_is_at_respective_stage(self):
        client = LeadProcess.objects.get(service = "Software")
        self.assertEqual(client.stage, 3)

# Login test

class UserTest(TestCase):

    def setUp(self):
        User.objects.create(
            username="akash", password="iamadangerousman")
        User.objects.create(
            username="ram", password="ramshyam")

    def test_sample_user_login(self):
        user_akash = User.objects.get(username='akash')
        self.assertEqual(user_akash.password, "iamadangerousman")
    
    def test_user_ram_login(self):
        user_ram = User.objects.get(username='ram')
        self.assertEqual(user_ram.password, 'ramshyam')