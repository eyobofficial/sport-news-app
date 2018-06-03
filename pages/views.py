from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'
