from django.contrib import admin
from django.urls import path
from app.views.product_view import ProductView
from app.views.category_view import CategoryView
from app.views.generate_product_view import GenerateProductView
from app.views.export_product_view  import ExportProductView

urlpatterns = [
    path('product/', ProductView.as_view(), name='product'),
    path('product/<pk>', ProductView.as_view(), name='product'),
    path('category/', CategoryView.as_view(), name='category'),
    path('generate-product/', GenerateProductView.as_view(), name='generate_product'),
    path('download-product/', ExportProductView.as_view(), name='download_product'),
]
