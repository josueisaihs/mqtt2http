from django.test import TestCase

from app.mapping.models import HTTPClient, MQTTBroker, TopicPattern, Endpoint, Mapping


class TestMapping(TestCase):
    def setUp(self):
        self.http_client = HTTPClient.objects.create(
            name="Test HTTP Client",
            host="http://test.http.client",
            port=80,
            username="test",
            password="test",
            description="This is a test HTTP client.",
        )
        self.mqtt_broker = MQTTBroker.objects.create(
            name="Test MQTT Broker",
            host="test.mqtt.broker",
            port=1883,
            username="test",
            password="test",
            description="This is a test MQTT broker.",
        )
        self.topic_pattern = TopicPattern.objects.create(
            name="Test Topic Pattern", pattern="test/topic/pattern"
        )
        self.endpoint = Endpoint.objects.create(
            name="Test Endpoint",
            endpoint="test/_doc",
            description="This is a test endpoint.",
        )

    def test_mapping(self):
        mapping = Mapping.objects.create(
            topic_pattern=self.topic_pattern,
            endpoint=self.endpoint,
            mqtt_broker=self.mqtt_broker,
            http_client=self.http_client,
        )
        self.assertEqual(mapping.topic_pattern, self.topic_pattern)
        self.assertEqual(mapping.endpoint, self.endpoint)
        self.assertEqual(mapping.mqtt_broker, self.mqtt_broker)
        self.assertEqual(mapping.http_client, self.http_client)
        self.assertEqual(
            str(mapping), "Test Topic Pattern - Test MQTT Broker - Test HTTP Client"
        )
        self.assertEqual(mapping.endpoint_url, "http://test.http.client/test/_doc")
