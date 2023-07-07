from django.urls import path
from api import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='book-list'),
    path('<int:pk>/',views.ProductDetail.as_view(), name='book-deatail'),
]
