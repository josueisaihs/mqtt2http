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

    def test_only_one_active(self):
        http_client_1 = HTTPClient.objects.create(
            name="Test HTTP Client 1",
            host="http://test.http.client",
            port=80,
            username="test",
            password="test",
            description="This is a test HTTP client.",
            is_active=True,
        )

        http_client_2 = HTTPClient.objects.create(
            name="Test HTTP Client 2",
            host="http://test.http.client",
            port=80,
            username="test",
            password="test",
            description="This is a test HTTP client.",
            is_active=True,
        )

        http_client_1.refresh_from_db()
        self.assertFalse(http_client_1.is_active)
        self.assertTrue(http_client_2.is_active)

        result = HTTPClient.objects.get_active().count()  # type: ignore
        expected = 1

        self.assertEqual(result, expected)
