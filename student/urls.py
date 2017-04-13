from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_groups, name='list_groups'),
	url(r'^(?P<group_id>[0-9]+)/$', views.list_students, name='list_students'),
    url(r'student/(?P<pk>[0-9]+)/edit$', views.StudentEditView.as_view(), name="edit_student"),
    url(r'student/new$', views.StudentCreateView.as_view(), name="create_student"),
    url(r'group/(?P<pk>[0-9]+)/edit$', views.GroupEditView.as_view(), name="edit_group"),
    url(r'group/(?P<pk>[0-9]+)/delete$', views.GroupDeleteView.as_view(), name="delete_group"),
    url(r'group/new$', views.GroupCreateView.as_view(), name="create_group"),
]