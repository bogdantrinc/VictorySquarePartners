from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', login_required(views.IndexView.as_view(), login_url='/login/'), name='index'),
    path('<int:pk>/', login_required(views.DetailView.as_view(), login_url='/login/'), name='detail'),
    path('<int:pk>/more/', login_required(views.more_details, login_url='/login/'), name='more'),
]
