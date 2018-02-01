# from django.test import TestCase
# from django.contrib.auth.models import User

# from rest_framework.authtoken.models import Token

# from ..models import LeadProcess


# class LeadProcessTest(TestCase):
#     """ Test module for leadprocess model """

#     def setUp(self):
#         user = User.objects.create(username="nerd")
#         LeadProcess.objects.create(
#             post_type='Top Jobs', amount=10000, billing_name='Apple', bulk='True', user=user)
#         LeadProcess.objects.create(
#             post_type='Hot Jobs', amount=10000, billing_name='Orange', bulk='True', user=user)

#     def test_leadprocess_billing_name(self):
#         leadprocess_top_jobs = LeadProcess.objects.get(post_type='Top Jobs')
#         leadprocess_hot_jobs = LeadProcess.objects.get(post_type='Hot Jobs')
#         self.assertEqual(
#             leadprocess_top_jobs.get_billing_name(), "Top Jobs has billing name Apple")
#         self.assertEqual(
#             leadprocess_hot_jobs.get_billing_name(), "Hot Jobs has billing name Orange")

#     def test_get_lead_object_with_billing_name(self):
#         lead_process = LeadProcess.objects.get(post_type="Hot Jobs")
#         self.assertEqual(lead_process.billing_name, "Orange")

#     def test_post_type_is_at_respective_amount(self):
#         client = LeadProcess.objects.get(post_type = "Top Jobs")
#         self.assertEqual(client.amount, 10000)

# # Login test

# class UserTest(TestCase):

#     def setUp(self):
#         User.objects.create(
#             username="akash", password="iamadangerousman")
#         User.objects.create(
#             username="ram", password="ramshyam")

#     def test_sample_user_login(self):
#         user_akash = User.objects.get(username='akash')
#         self.assertEqual(user_akash.password, "iamadangerousman")
    
#     def test_user_ram_login(self):
#         user_ram = User.objects.get(username="ram")
#         self.assertEqual(user_ram.password, "ramshyam")

#     # def test_token(self):
#     #     user = User.objects.create(username="khaikoho")
#     #     user_akash = Token.objects.get(user=user)
#     #     self.assertEqual(user_akash.key, "kaka")