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
            description="This is a test MQTT broker.",
        )
        self.assertEqual(mqtt_broker.name, "Test MQTT Broker")
        self.assertEqual(mqtt_broker.host, "test.mqtt.broker")
        self.assertEqual(mqtt_broker.port, 1883)
        self.assertEqual(mqtt_broker.username, "test")
        self.assertEqual(mqtt_broker.password, "test")
        self.assertEqual(mqtt_broker.description, "This is a test MQTT broker.")
        self.assertEqual(str(mqtt_broker), "Test MQTT Broker")

    def test_only_one_active(self):
        mqtt_broker_1 = MQTTBroker.objects.create(
            name="Test MQTT Broker 1",
            host="test.mqtt.broker",
            port=1883,
            username="test",
            password="test",
            description="This is a test MQTT broker.",
            is_active=True,
        )

        mqtt_broker_2 = MQTTBroker.objects.create(
            name="Test MQTT Broker 2",
            host="test.mqtt.broker",
            port=1883,
            username="test",
            password="test",
            description="This is a test MQTT broker.",
            is_active=True,
        )

        mqtt_broker_1.refresh_from_db()
        self.assertFalse(mqtt_broker_1.is_active)
        self.assertTrue(mqtt_broker_2.is_active)

        result = MQTTBroker.objects.get_active().count()  # type: ignore
        expected = 1

        self.assertEqual(result, expected)
