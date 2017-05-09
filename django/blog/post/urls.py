from django.conf.urls import include, url

import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post-detail'),
    url(r'^create-post/$', views.create_post, name='post-create'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout')
]
