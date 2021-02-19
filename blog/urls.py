from django.urls import path
from blog import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='about')
]
