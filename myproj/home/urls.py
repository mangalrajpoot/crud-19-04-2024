from django.urls import path 
from . import views 

urlpatterns=[
    path('',views.create,name='create'),
    path('read',views.read,name='read'),
    path('edit',views.edit,name='edit'),
    path('delete',views.delete,name='delete'),
    

]