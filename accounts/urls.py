from django.conf.urls import include, url

from . import views

urlpatterns = [
        url('^register/', views.register,name="register"),
        # url('^logout', views.logout_view,name="logout"),
        # url('^login', views.logout_view,name="login"),
        url(r'^login/$', 'django.contrib.auth.views.login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
        url(r'^', include('django.contrib.auth.urls')),
        url(r'^myprofile/', views.myprofile, name='myprofile'),
        url(r'^users/', views.user_profilelist, name='user_profilelist'),
        url(r'^editprofile/', views.profile_edit, name='profile_edit'),
        url(r'^(?P<id>\d+)$', views.user_profiles, name='user_profiles'),
         
]