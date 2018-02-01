# from django.urls import reverse

# from rest_framework import status
# from rest_framework.test import APITestCase

# from ..models import (
#     Branch,
#     BusinessOutflow,
#     ListService
#     )

# class BranchTests(APITestCase):

#     def test_create_branch(self):
#         """
#         Ensure we can create a new Branch object.
#         """
#         url = reverse('get_post_branch')
#         data = {
#             "branch_incharge": "Ram Kaji",
#             "branch_address": "Bhaktapur",
#             "branch_phone": 9999999999,
#             "branch_email": "dope@guy.com"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Branch.objects.count(), 1)
#         self.assertEqual(Branch.objects.get().branch_incharge, 'Ram Kaji')

# class ListServiceTests(APITestCase):

#     def test_create_listservice(self):
#         """
#         Ensure we can create a new ListService object.
#         """
#         url = reverse('get_post_listservice')
#         data = {
#             "service_name": "My Service",
#             "service_detail": "This is dope!"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(ListService.objects.count(), 1)
#         self.assertEqual(ListService.objects.get().service_name, 'My Service')

# class BusinessOutflowTests(APITestCase):

#     def test_create_businessoutflow(self):
#         """
#         Ensure we can create a new BusinessOutflow object.
#         """
#         url = reverse('get_post_businessoutflow')
#         data = {
#             "outflowed_to": "KMG",
#             "service_outflowed": "Test",
#             "outflow_date": "2018-01-01",
#             "amount": 150000
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(BusinessOutflow.objects.count(), 1)
#         self.assertEqual(BusinessOutflow.objects.get().outflowed_to, 'KMG')