from django.urls import path, include

from .views import savat, order

app_name = "orders"

urlpatterns = [
    path('', savat, name="savat"),
    path('order/', order, name="order"),
]

