from django.urls import path
from . import views



urlpatterns = [
    path('', views.CartItemView.as_view(), name="cart"),
    path('add/', views.CartItemAddView.as_view()),
    path('delete/<int:pk>/', views.CartItemDeleteView.as_view()),
]