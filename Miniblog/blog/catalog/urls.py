from django.urls import path
from . import views

 #manages catalog urls
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>/',views.BloggerDetailView.as_view(), name='author-detail'),
]

