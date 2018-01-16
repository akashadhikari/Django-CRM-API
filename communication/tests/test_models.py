from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Clientlist, SalesStage, SalesSub
from lead.models import LeadProcess


class ClientlistTest(TestCase):
    """ Test module for Clientlist model """

    def setUp(self):
        user = User.objects.create(username="nerd")
        lead = LeadProcess.objects.create(service_type="Hardware", user=user)
        Clientlist.objects.create(
            client_name='Apple', contact_person='Mr. Foo Bar', client_pic='.common/files/images/display.png', user=user, lead=lead)
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

class SalesStageTest(TestCase):

    def setUp(self):
        user = User.objects.create(username="nerd")
        lead = LeadProcess.objects.create(service_type="Hardware", user=user)
        client = Clientlist.objects.create(client_name="Apple", user = user, lead = lead)
        SalesStage.objects.create(
            substage = 'Contact verification', sales_stage= 'Suspecting', client = client, user = user)
        SalesStage.objects.create(
            substage = 'Client detail', sales_stage='Prospecting', client = client, user = user)

    def test_salesstage_status(self):
        salesstage_suspecting = SalesStage.objects.get(sales_stage='Suspecting')
        salesstage_prospecting = SalesStage.objects.get(sales_stage = 'Prospecting')
        self.assertEqual(
            salesstage_suspecting.get_substage(), "Contact verification falls under Suspecting")
        self.assertEqual(
            salesstage_prospecting.get_substage(), "Client detail falls under Prospecting")

# class SalesSubTest(TestCase):

#     def setUp(self):
#         user = User.objects.create(username="nerd")
#         lead = LeadProcess.objects.create(service_type="Hardware", user=user)
#         client = Clientlist.objects.create(client_name="Apple", user = user, lead = lead)
#         substage = SalesStage.objects.create(substage="Contact verification", client = client)
#         SalesSub.objects.create(
#             sales_substage = 'Verified', substage = substage, client = client)
#         SalesSub.objects.create(
#             sales_substage = 'Detailed', substage = substage, client = client)

#     def test_salessubstage_status(self):
#         salessubstage_verified = SalesSub.objects.get(sales_substage = 'Verified')
#         salessubstage_detailed = SalesSub.objects.get(sales_substage = 'Detailed')
#         self.assertEqual(
#             salessubstage_verified.get_salessubstage(), "Contact verification childrens to Verified")
#         self.assertEqual(
#             salessubstage_detailed.get_salessubstage(), "Client detail childrens to Detailed")
