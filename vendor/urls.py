from django.urls.conf import path, include
from rest_framework import routers
from . import views

app_name = 'product'
router = routers.DefaultRouter()
router.register('product_list', views.ProductListView)
# router.register('product_create', views.ProductCreateView)

urlpatterns = [
    #   path("", views.ProductListView.as_view(), name="post users"),
    path('', include(router.urls))
]
