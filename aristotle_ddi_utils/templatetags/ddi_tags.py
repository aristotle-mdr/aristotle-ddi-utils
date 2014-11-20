from django import template
register = template.Library()

@register.simple_tag
def make_urn(item):
    if item.version:
        version = item.version
    else:
        version = "1.0.0"
    urn = 'urn:ddi:%s:%s:%s'%('example.com',item.id,version)
    return urn
