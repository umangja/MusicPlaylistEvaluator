from django.conf.urls import url
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('showAllRating',views.showAllRating,name='showAllRating'),
    path('updateTimeLimit',views.updateTimeLimit,name='updateTimeLimit'),
    path('showAllRatingForParticularUser',views.showAllRatingForParticularUser,name='showAllRatingForParticularUser')
]

