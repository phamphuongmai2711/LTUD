from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('san-pham/', views.product_list, name='product_list'),
    path('san-pham/<int:pk>/', views.product_detail, name='product_detail'),
    path('gioi-thieu/', views.about, name='about'),
    path('tin-tuc/', views.news, name='news'),
    path('tin-tuc/<int:pk>/', views.post_detail, name='post_detail'),
    path('lien-he/', views.contact, name='contact'),
]