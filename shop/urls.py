from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

#if settings.DEBUG:
#    urlpatterns += [
#        url(r'^media/(?P<path>.*)$', serve, {
#            'document_root':settings.MEDIA_ROOT,
#        }),
#        
#    ]