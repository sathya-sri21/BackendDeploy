from django.urls import path;
from .views import *
urlpatterns=[
    path('create',ProductCRUDAPI.as_view()),
    path('read',ProductCRUDAPI.as_view()),
    path('read/<int:product_id>',ProductCRUDAPI.as_view()),
    path('edit/<int:product_id>',ProductCRUDAPI.as_view()),
    path('delete/<int:product_id>',ProductCRUDAPI.as_view()),
    path('crud',ProductCRUD),
    path('products/',ProductAddandGet.as_view()),
    path('products/<int:pk>',ProductUpdateandDelete.as_view())

]