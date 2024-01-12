from django import template

register = template.Library()


@register.filter
def unique_categories(items):
    return ["App", "Card", "Web"]