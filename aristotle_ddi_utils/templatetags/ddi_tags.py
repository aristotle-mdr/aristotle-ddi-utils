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

def value_type(item):

    type_map = {
        #"":"Code",
        "Date/Time":"DateTime",
        #"":"ExternalCategory",
        #"":"GeographicLocationCode",
        #"":"GeographicStructureCode",
        "Number":"Numeric",
        "Currency":"Numeric",
        #"":"Scale",
        "String":"Text"
    }
    value_type = "Text"
    num_values = item.permissiblevalue_set.all().count()
    if item.data_type and num_values == 0:
        value_type = type_map.get(item.data_type.name)
    elif num_values > 0:
        value_type = "Code"

@register.filter
def valuedomain_dditype(item):
    return "r:Managed" + value_type(item) + "Representation"

@register.filter
def valuedomain_managed_dditype(item):
    return "r:" + value_type(item) + "Representation"