from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from . import models


class IndexView(TemplateView):
    template_name = 'news/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_name'] = 'መነሻ'
        return context


class TagDetailView(DetailView):
    model = models.Tag

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        tag = get_object_or_404(models.Tag, pk=self.kwargs['pk'])
        context['post_list'] = tag.posts.filter(status=1)
        return context


class PostList(ListView):
    model = models.Post
    paginate_by = 7

    def get_queryset(self, *args, **kwargs):
        tag = get_object_or_404(models.Tag, slug=self.kwargs['slug'])
        return tag.posts.filter(status=1)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        tag = get_object_or_404(models.Tag, slug=self.kwargs['slug'])
        context['page_name'] = tag.title
        return context


def tag_detail(request, pk, slug):
    tag = get_object_or_404(models.Tag, pk=pk)
    posts = tag.posts.filter(status=1)
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    page_name = tag.title
    return render(request, 'news/tag_detail.html', {
        'post_list': post_list,
        'page_name': page_name,
    })


class TransferView(TemplateView):
    template_name = 'news/transfer.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        transfer_tag = models.Tag.objects.get(slug='transfer')
        context['post_list'] = transfer_tag.posts.filter(status=1)
        return context


class PostDetailView(DetailView):
    model = models.Post