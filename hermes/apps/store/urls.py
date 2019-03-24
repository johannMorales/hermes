from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from hermes.apps.store.views import PaymentConditionListAPIView, ProductView
from .views import ( MeasureUnitListAPIView )

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^measure_units/?$', MeasureUnitListAPIView.as_view()),
    url(r'^payment_conditions/?$', PaymentConditionListAPIView.as_view()),
    url(r'^products/?$', ProductView.as_view()),
]
