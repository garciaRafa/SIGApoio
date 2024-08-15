from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from json import dumps


class TestFront(TestCase):
    def setUp(self):
        self.client = APIClient()