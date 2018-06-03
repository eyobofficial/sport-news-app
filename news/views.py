from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from . import models


class IndexView(TemplateView):
    template_name = 'news/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['breaking_post_list'] = models.Post.objects.breaking()[:10]
        context['featured_post_list1'] = models.Post.objects.featured()[:3]
        context['featured_post_list2'] = models.Post.objects.featured()[3:5]

        # Latest News
        context['latest_post1'] = models.Post.objects.non_featured()[0]
        context['latest_post_list1'] = models.Post.objects.non_featured()[1:6]

        context['popular_post_list'] = models.Post.objects.popular()[:6]

        context['more_post_list'] = models.Post.objects.non_featured()[6:]
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


def post_detail(request, pk, slug):
    post = get_object_or_404(models.Post, pk=pk, slug=slug)
    post.read_count = post.read_count + 1
    post.save()
    return render(request, 'news/post_detail.html', {
        'post': post,
    })