from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('checkout/', views.payment_checkout, name='checkout_payment'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
]