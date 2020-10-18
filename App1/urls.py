from django.conf.urls import url
from . import views

app_name = 'App1'

urlpatterns = [
    url('', views.home, name='home'),
    # url('login', views.FormView.as_view(), name='login'),
    url('register', views.SignUp, name='register'),

]

