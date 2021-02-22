from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('/about', views.AboutView.as_view(), name='about'),
    path('/post/<slug:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('/post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('/post/<slug:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('/post/<slug:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('/drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('/post/<slug:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('/post/<slug:pk>/comment_approve/', views.comment_approve, name='comment_approve'),
]
