from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^posts/$', views.PostListView.as_view(), name='post_list'),
	url(r'^posts/top/$', views.TopPostListView.as_view(), name='post_top'),
	url(r'^posts/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/' \
			r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
	url(r'^posts/rate/$', views.post_rate, name='post_rate'),
	url(r'^posts/add/$', views.post_add, name='post_add'),
	url(r'^categories/$', views.CategoryListView.as_view(), name='category_list'),
	url(r'^categories/(?P<category>[-\w]+)/$', views.category_detail, name='category_detail'),
]