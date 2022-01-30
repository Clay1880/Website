from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('buy_pistol', views.buy_pistol, name='buy_pistol'),
    path('payment', views.payment, name='payment'),
    path('buy_rifle',views.buy_rifle, name="buy_rifle"),
    path('payment_rifle',views.payment_rifle, name="payment_rifle"),
    path('buy_shotgun',views.buy_shotgun, name="buy_shotgun"),
    path('payment_shotgun',views.payment_shotgun, name="payment_shotgun"),
    path('buy_snipers',views.buy_snipers, name="buy_snipers"),
    path('payment_sniper',views.payment_sniper, name="payment_sniper"),
    path('buy_submachinegun',views.buy_submachinegun, name="buy_submachinegun"),
    path('payment_smg',views.payment_smg, name="payment_smg")
]
