from django import template
register = template.Library()

@register.simple_tag
def make_urn(item):

    from django.conf import settings
    agency = getattr(settings, 'ARISTOTLE_DDI_AGENCY', "example.com")

    if item.version:
        version = item.version
    else:
        version = "1.0.0"
    urn = 'urn:ddi:%s:%s:%s'%(agency,item.id,version)
    return urn
