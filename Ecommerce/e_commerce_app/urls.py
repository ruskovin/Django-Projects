from django.urls import path
from . import views
# url patterns here

app_name = "e_commerce_app"
urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('item/<slug:slug>', views.ItemDetailView.as_view(), name='item'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart')
]