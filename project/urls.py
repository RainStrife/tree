from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tree/', views.get_tree),
    url(r'^graph/', views.get_graph),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
