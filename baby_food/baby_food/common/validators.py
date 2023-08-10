import datetime
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


def validate_birth_date(value):
    six_months_days = 182
    three_years_days = 1095

    current_date = datetime.date.today()
    current_age = (current_date - value)

    if current_age.days < six_months_days:
        raise ValidationError(f'The child age should be at least 6-months.')
    if current_age.days > three_years_days:
        raise ValidationError(f'The child age should be less than 3-years.')
