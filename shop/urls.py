from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
               url(r'', views.main, name='main'),
               url(r'^$', views.about, name='about'),
               url(r'^$', views.stores, name='stores'),
               ]

#if settings.DEBUG:
#urlpatterns += [
                    #url(r'^media/(?P<path>.*)$', {
            #'document_root':settings.MEDIA_ROOT,
            # }),
                    #
                    #    ]
