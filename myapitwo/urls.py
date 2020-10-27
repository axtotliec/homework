# myapi/urls.py
from django.urls import path #, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categorys', views.CategoryViewSet)
router.register(r'tableones', views.TableoneViewSet)
router.register(r'tabletwos', views.TabletwoViewSet)
router.register(r'tablethrees', views.TablethreeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls