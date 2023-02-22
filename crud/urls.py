from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<id>', views.delete_user, name='delete'),
    path('update/<id>', views.update_user, name='update')
]