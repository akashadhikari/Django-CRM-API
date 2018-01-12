from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Clientlist
from lead.models import LeadProcess


class ClientlistTest(TestCase):
    """ Test module for Clientlist model """

    def setUp(self):
        user = User.objects.create(username="nerd")
        lead = LeadProcess.objects.create(service="Hardware", user=user)
        Clientlist.objects.create(
            client_name='Apple', contact_person='Mr. Foo Bar', user=user, lead=lead)
        Clientlist.objects.create(
            client_name='Orange', contact_person='Mr. Foo Bar', user=user, lead=lead)

    def test_clientlist_status(self):
        clientlist_apple = Clientlist.objects.get(client_name='Apple')
        clientlist_orange = Clientlist.objects.get(client_name='Orange')
        self.assertEqual(
            clientlist_apple.get_contact_person(), "Apple is in touch with Mr. Foo Bar")
        self.assertEqual(
            clientlist_orange.get_contact_person(), "Orange is in touch with Mr. Foo Bar")

    def test_contact_person_looks_after_clients(self):
        new_client = Clientlist.objects.get(client_name="Apple")
        self.assertEqual(new_client.contact_person, "Mr. Foo Bar")