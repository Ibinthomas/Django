from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('view/<id>',views.view_movie),

]