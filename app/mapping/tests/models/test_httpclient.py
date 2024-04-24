from django.test import TestCase

from app.mapping.models import HTTPClient


class TestHTTPClient(TestCase):
    def test_http_client(self):
        http_client = HTTPClient.objects.create(
            name="Test HTTP Client",
            host="http://test.http.client",
            port=80,
            username="test",
            password="test",
            description="This is a test HTTP client.",
        )

        self.assertEqual(http_client.name, "Test HTTP Client")
        self.assertEqual(http_client.host, "http://test.http.client")
        self.assertEqual(http_client.port, 80)
        self.assertEqual(http_client.method, "POST")
        self.assertEqual(http_client.username, "test")
        self.assertEqual(http_client.password, "test")
        self.assertEqual(http_client.description, "This is a test HTTP client.")
        self.assertEqual(str(http_client), "Test HTTP Client")
