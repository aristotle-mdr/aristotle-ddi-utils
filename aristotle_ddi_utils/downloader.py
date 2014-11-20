#aristotle_ddi_utils
from aristotle_mdr.utils import get_download_template_path_for_item
from django.shortcuts import render

def download(request,downloadType,item):

    template = get_download_template_path_for_item(item,downloadType)

    response = render(request,template,
        {'item':item,
        },
        content_type='application/xml'
        )
    #response['Content-Disposition'] = 'attachment; filename=%s.ddi.xml'%item.id
    return response
