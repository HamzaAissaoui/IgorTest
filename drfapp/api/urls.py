from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'demography', views.DemographyViewSet)
urlpatterns = [url(r'^', include(router.urls))]