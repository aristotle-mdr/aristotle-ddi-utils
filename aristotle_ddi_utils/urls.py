from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
#These are required for about pages to work. Include them, or custom items will die!
#    url(r'^about/(?P<template>.+)/?$', views.DynamicTemplateView.as_view(), name="about"),
    url(r'^/?$', TemplateView.as_view(template_name='aristotle_ddi_utils/about_aristotle_ddi.html'), name="about"),
    url(r'^about/?$', TemplateView.as_view(template_name='aristotle_ddi_utils/about_aristotle_ddi.html'), name="about"),
]