from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from restaurant.views import *
import json


class MenuViewTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username='test', password='test')
        self.menu = Menu.objects.create(title='Tea', price=10, inventory=100)
        self.menu.save()

    def test_getall(self):
        request = self.factory.get('/api/tables')
        request.user = self.user
        response = BookingViewSet.as_view({'get': 'list'})(request)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().title, 'Tea')