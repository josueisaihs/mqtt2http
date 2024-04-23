from django.core.exceptions import ValidationError

from app.config.validators import validation_pattern

def test_validation_pattern():
    valid_pattern = "test/+/pattern"
    
    assert validation_pattern(valid_pattern) == valid_pattern

def test_validation_pattern_wrong():
    patterns = (
        "test/topic/pattern#/",
        "test/#topic/pattern/#",
        "test/topic/pattern /",
        "/test/topic/pattern",
        "test/topic/pattern/",
        "test//topic/pattern",
        "a" * 1001,
        "",
        "".join(["a" for _ in range(1001)])
    )
    for pattern in patterns:
        try:
            validation_pattern(pattern)
            assert False
        except ValidationError:
            assert True
