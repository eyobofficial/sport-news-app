from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from . import models


class IndexView(TemplateView):
    template_name = 'news/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_name'] = 'home'
        return context


class TransferView(TemplateView):
    template_name = 'news/transfer.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        transfer_tag = models.Tag.objects.get(slug='transfer')
        context['post_list'] = transfer_tag.posts.filter(status=1)
        return context


class PostDetailView(DetailView):
    model = models.Post