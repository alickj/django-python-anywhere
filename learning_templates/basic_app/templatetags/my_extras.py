from django import template
# This demonstrates setting up a c custom filter

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, '')


# register.filter('cut', cut)
