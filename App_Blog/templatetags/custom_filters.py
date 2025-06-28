from django import template

register = template.Library()

def range_filter(value):
    return value[0:500] + "......."

register.filter('range_filters',range_filter)