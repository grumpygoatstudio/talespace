from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user', views.user_add, name='user_add'),
    url(r'^user/(?P<user_id>[0-9]+)', views.user_profile, name='user_profile'),
    url(r'^tales/(?P<tale_id>[0-9]+)', views.tale_details, name='tale_details'),
    url(r'^tales/', views.tales_list, name='tales_list'),
]