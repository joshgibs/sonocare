from django.urls import path

from . import views

urlpatterns = [
    path('payments-dev/', views.paymentsdev, name='payments-dev'),
    path('payments/', views.payments, name='payments'),
    path('', views.index, name='index'),
]