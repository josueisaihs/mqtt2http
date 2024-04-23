from django.core.exceptions import ValidationError

def validation_pattern(value):
    def validator(value):
        if "#" in value:
            if value.count("#") > 1:
                raise ValidationError("The topic pattern can only have one wildcard character '#' at the end of the string.")
            if not value.endswith("#"):
                raise ValidationError("The topic pattern can only have one wildcard character '#' at the end of the string.")
        
        # if not all(c in [string.ascii_letters + string.digits + "/" + "#" + "+"] for c in value):
        #    raise ValidationError(f"The topic pattern <{value}> can only have alphanumeric characters.")
        
        if len(value) > 1000:
            raise ValidationError("The topic pattern can only have a maximum of 1000 characters.")
        
        if len(value) < 1:
            raise ValidationError("The topic pattern must have at least one character.")
        
        if value.startswith("/"):
            raise ValidationError("The topic pattern cannot start with a slash '/'.")
        
        if value.endswith("/"):
            raise ValidationError("The topic pattern cannot end with a slash '/'.")
        
        if "//" in value:
            raise ValidationError("The topic pattern cannot have two slashes '//' together.")
        
        return value        
    return validator(value)
