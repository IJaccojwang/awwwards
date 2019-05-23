from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'profile/edit$',views.edit_profile,name='edit'),
    url(r'^project/new$', views.new_project, name='post'),
    url(r'^project$',views.project,name='project'),
    url(r'^search/',views.search,name='search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)