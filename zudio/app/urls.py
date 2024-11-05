from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),
    path('register',views.register),

#-------------admin--------------------


path('shop_home',views.shop_home),
path('add_pro',views.add_product),
path('edit_pro/<id>',views.edit_pro),
path('delete_pro/<id>',views.delete_pro),


#-------------user---------------------+
path('user_home',views.user_home),
path('views_pro/<id>',views.views_pro),
path('add_cart/<pid>',views.add_cart),
path('cart_display',views.cart_display),
path('delete_cart/<id>',views.delete_cart),
path('buy_pro/<id>',views.buy_pro),
path('view_booking',views.user_view_booking),



]