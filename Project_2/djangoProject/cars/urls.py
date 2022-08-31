from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/more/', views.more_details, name='more'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
]
