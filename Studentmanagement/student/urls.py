from django.urls import path
from . import views

urlpatterns=[
    path('dis',views.disp_std),
    path('add_std',views.add),
    path('edit_std/<id>',views.edit_std),
    path('delete_std/<id>',views.delete_std),


]