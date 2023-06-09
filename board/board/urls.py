from django.urls import path
from . import views

app_name='board'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('detail/<bpk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<bpk>', views.update, name='update'),
    path('delete/<bpk>', views.delete, name='delete')
]