from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomerList.as_view(), name='list'),
    path('detail/<int:pk>/', views.CustomerDetail.as_view(), name='detail'),
    path('create/', views.CustomerCreate.as_view(), name='create'),
    path('update/<int:pk>', views.CustomerUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.CustomerDelete.as_view(), name='delete'),
]
