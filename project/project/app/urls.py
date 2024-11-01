from django.urls import path
from . import views

urlpatterns=[
    path('s',views.fun1),
    path('a',views.fun2),
    path('fun/<a>/<b>',views.fun3),
    path("fun4/<int:a>/<int:b>/<int:c>",views.fun4),
    path('index',views.index_page),
    path('demo',views.demo),
    path('second',views.second),
    path('tudo',views.tudo1),
    path('edit/<id>',views.edit_form),
    path('delete/<id>',views.delt_fun),

]