from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from app.mapping.models import TopicPattern

# Create your tests here
class TestTopicPattern(TestCase):
    def test_topic_pattern(self):
        topic_pattern = TopicPattern.objects.create(
            name="Test Topic Pattern",
            pattern="test/topic/pattern",
            description="This is a test topic pattern."
        )
        self.assertEqual(topic_pattern.name, "Test Topic Pattern")
        self.assertEqual(topic_pattern.pattern, "test/topic/pattern")
        self.assertEqual(topic_pattern.description, "This is a test topic pattern.")
        self.assertEqual(str(topic_pattern), "Test Topic Pattern - test/topic/pattern")
    
    def test_topic_wrong_pattern(self):
        pattern = "test/topic/pattern#/"
        with self.assertRaises(ValidationError):
            TopicPattern.objects.create(
                name="Test Topic Pattern",
                pattern=pattern,
                description="This is a test topic pattern."
            ).full_clean()
        
    def test_topic_unique_pattern(self):
        topic_pattern = TopicPattern.objects.create(
            name="Test Topic Pattern",
            pattern="test/topic/pattern",
            description="This is a test topic pattern."
        )

        topic_pattern.full_clean()

        with self.assertRaises(IntegrityError):
            TopicPattern.objects.create(
                name="Test Topic Pattern",
                pattern="test/topic/pattern",
                description="This is a test topic pattern."
            )
