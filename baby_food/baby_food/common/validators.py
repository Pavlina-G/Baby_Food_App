from datetime import datetime
import string

from django.core.exceptions import ValidationError


def validate_card_number(value):
    if len(str(value)) == 16 and isinstance(value, int):
        return value
    else:
        raise ValidationError('Card number must contain 16 digits')


def validate_name(value):
    text = ''.join(value.split(' '))
    allowed = string.ascii_letters + '-'

    for ch in text:
        if ch not in allowed:
            raise ValidationError(
                message='Enter a valid name',
                code='invalid',
            )
