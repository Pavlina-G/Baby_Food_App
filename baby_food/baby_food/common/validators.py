from django.core.exceptions import ValidationError


def validate_card_number(value):
    if len(str(value)) == 16 and isinstance(value, int):
        return value
    else:
        raise ValidationError('Card number must contain 16 digits')