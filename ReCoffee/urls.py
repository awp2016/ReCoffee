from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^user/(?P<pk>\d+)/$', views.user_profile,
        name="user_profile"),
    url(r'^shop/(?P<pk>\d+)/$', views.shop_profile,
        name="shop_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
