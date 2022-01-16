from django.urls.conf import path, include
from rest_framework import routers
from . import views

app_name = 'product'
router = routers.DefaultRouter()
router.register('product_list', views.ProductListView)
router.register('color_list', views.ColorListView)
router.register('size_list', views.SizeListView)

urlpatterns = [
    #   path("", views.ProductListView.as_view(), name="post users"),
    path('', include(router.urls))
]
