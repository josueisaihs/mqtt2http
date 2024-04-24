from django.test import TestCase

from app.mapping.models import Endpoint


class TestEndpoint(TestCase):
    def test_endpoint(self):
        endpoint = Endpoint.objects.create(
            name="Test Endpoint",
            endpoint="test/endpoint",
        )
        self.assertEqual(endpoint.name, "Test Endpoint")
        self.assertEqual(endpoint.endpoint, "test/endpoint")
