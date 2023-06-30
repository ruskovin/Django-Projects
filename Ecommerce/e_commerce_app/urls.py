from django.urls import path
from . import views
# url patterns here

app_name = "e_commerce_app"
urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
    path('item/<slug:slug>', views.ItemDetailView.as_view(), name='item'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
]