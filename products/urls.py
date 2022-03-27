from django.urls import path
from .views import ProductDetailView
from .views import ProductSearchListView

urlpatterns = [
#   path('<pk>', ProductDetailView.as_view(), name='product'),
    path('search', ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', ProductDetailView.as_view(), name='product'),
       
    ]