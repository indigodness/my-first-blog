from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
               path('', views.main, name='main'),
               path('about/', views.about, name='about'),
               path('stores/', views.stores, name='stores'),
               path('bakery/', views.bakery, name='bakery'),
               path('cereal/', views.cereal, name='cereal'),
               path('diary/', views.diary, name='diary'),
               path('drinks/', views.drinks, name='drinks'),
               path('frozen/', views.frozen, name='frozen'),
               path('meat/', views.meat, name='meat'),
               path('snack/', views.snack, name='snack'),
               path('vegan/', views.vegan, name='vegan'),
               ]

#if settings.DEBUG:
#urlpatterns += [
                    #url(r'^media/(?P<path>.*)$', {
            #'document_root':settings.MEDIA_ROOT,
            # }),
                    #
                    #    ]
