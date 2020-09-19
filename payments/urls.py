from django.urls import path

from . import views

urlpatterns = [
    path('', views.paymentView, name='payment'),
    path('config/', views.stripe_config),  # new
]
