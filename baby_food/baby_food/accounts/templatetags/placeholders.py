from django.template import Library

register = Library()


@register.filter
def placeholder(field, text):
    field.field.widget.attrs['placeholder'] = text
    return field


@register.filter(name='times')
def times(number):
    return range(number)

@register.filter()
def multiply(value, arg):
    return float(value) * arg




