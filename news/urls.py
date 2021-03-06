from django.urls import path
from . import views


app_name = 'news'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('transfers/', views.TransferView.as_view(), name='transfers'),
    path('post/<int:pk>/<str:slug>', views.post_detail, name='post-detail'),
    path('<str:slug>', views.PostList.as_view(), name='post-list'),
]
