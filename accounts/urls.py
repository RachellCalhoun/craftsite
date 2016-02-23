from django.conf.urls import include, url

from . import views

urlpatterns = [
        url('^register/', views.register,name="register"),
        # url('^logout', views.logout_view,name="logout"),
        # url('^login', views.logout_view,name="login"),
        url(r'^login/$', 'django.contrib.auth.views.login'),
        url('^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
        url('^', include('django.contrib.auth.urls')),
        url(r'^myprofile/', views.user_profiles, name='user_profile'),
        url(r'^users/', views.user_profilelist, name='user_profilelist'),
        url(r'^editprofile/', views.profile_edit, name='profile_edit'),
        url(r'^profile/(?P<pk>[0-9]+)/$', views.user_profiles, name='user_profile'),
]