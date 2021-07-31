from django.urls import path
from .import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>',views.post_detail, name='post_detail'),
    path('contacts',views.contacts, name='contacts'),
    path('about',views.about, name='about'),
    path('add_comment/<int:pk>',views.add_comment,name='add_comment'),
    
]
