'''定义learning_logs的URL模式'''
from django.urls import path
from django.conf.urls import url
from . import views
#app_name = 'learning_logs'
urlpatterns = [
    #path(”, include((‘names’, scores’), namespace=’scores’))
    #url(r'^$',views.index,name='index'),
    path('index',views.index,name='index'),
    path('',views.topics,name='topics'),
    #path('topics/', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
]