from django.urls import path
from . import views

app_name = 'coupons'
urlpatterns = [
    path("coupons/", views.coupon_apply, name="apply"),
]
