from django.conf.urls import patterns , url
from Alexandra import views

urlpatterns = patterns ( '',
  url(r'^$', views.index, name = 'index' ),
  url(r'^posts/', views.posts, name = 'posts'),
  )