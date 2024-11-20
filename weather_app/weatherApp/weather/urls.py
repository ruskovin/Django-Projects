from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('delete_city/<int:pk>', views.CityDeleteView.as_view(), name="delete_city")
]
