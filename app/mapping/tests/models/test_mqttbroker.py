from django.test import TestCase

from app.mapping.models import MQTTBroker


class TestMQTTBroker(TestCase):
    def test_mqtt_broker(self):
        mqtt_broker = MQTTBroker.objects.create(
            name="Test MQTT Broker",
            host="test.mqtt.broker",
            port=1883,
            username="test",
            password="test",
            description="This is a test MQTT broker."
        )
        self.assertEqual(mqtt_broker.name, "Test MQTT Broker")
        self.assertEqual(mqtt_broker.host, "test.mqtt.broker")
        self.assertEqual(mqtt_broker.port, 1883)
        self.assertEqual(mqtt_broker.username, "test")
        self.assertEqual(mqtt_broker.password, "test")
        self.assertEqual(mqtt_broker.description, "This is a test MQTT broker.")
        self.assertEqual(str(mqtt_broker), "Test MQTT Broker")
