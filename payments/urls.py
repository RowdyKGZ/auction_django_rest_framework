from django.conf.urls import url
from django.urls import path

from .views import checkout, create_payment_intent

urlpatterns = [
    url('create-charge/', checkout, name="count"),
    path('create/payment/<int:order_id>/', create_payment_intent, name='create-payment-intent'),
]
