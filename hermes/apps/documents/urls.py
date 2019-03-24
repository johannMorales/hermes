from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^add_boleta$', views.generate_boleta),
    url(r'^add_factura$', views.generate_factura),
    url(r'^add_cotizacion$', views.generate_cotizacion),
]

