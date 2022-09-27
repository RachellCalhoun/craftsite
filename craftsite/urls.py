from django.urls import  include, re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView

# from postman.views import WriteView


admin.autodiscover()


urlpatterns = [
	# re_path(r'^write/(?:(?P<recipients>[^/#]+)/)?$',
 #        WriteView.as_view()(template_name='my_custom_write.html'),
 #        name='write'),
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'^login/$', 'django.contrib.auth.views.login'),
    # re_path(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/crafts'}),
    re_path(r'^',include('crafts.urls', namespace='crafts')),
    re_path(r'^',include('accounts.urls', namespace='accounts')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^messages/', include('postman.urls', namespace='postman')),
    re_path(r'^$',TemplateView.as_view(template_name="landingpage.html")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
