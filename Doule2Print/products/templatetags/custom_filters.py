# products/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_price(variety, user):
    if hasattr(user, 'customer') and user.customer.is_wholesale:
        return variety.wholesale_price
    return variety.retail_price
