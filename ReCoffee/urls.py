from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register', views.register_view, name="register"),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^user/(?P<pk>\d+)/$', views.user_profile,
        name="user_profile"),
    url(r'^shop_profile/(?P<pk>\d+)/$', views.shop_profile,
        name="shop_profile"),
    url(r'^add_fave/(?P<shop_pk>\d+)/$', views.add_fave, name="faved"),
    url(r'^lista_cafenele/(?P<shopSearch>[\w\-]+)/$',
        views.lista_cafenele_view, name="lista_cafenele"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
