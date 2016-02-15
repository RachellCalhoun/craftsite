from django.conf.urls import include, url

from . import views

urlpatterns = [
        url('^register/', views.register,name="register"),
        # url('^logout', views.logout_view,name="logout"),
        # url('^login', views.logout_view,name="login"),
        url('^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
        url('^', include('django.contrib.auth.urls')),
]