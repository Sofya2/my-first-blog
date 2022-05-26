from django.urls import path
from . import views
from django.conf import url

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,})
]
