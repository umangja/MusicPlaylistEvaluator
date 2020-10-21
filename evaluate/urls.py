from django.urls import path
from . import views

urlpatterns = [
    path('evaluate', views.evaluate, name='evaluate'),
    path('saveRatings',views.saveRatings,name='saveRatings'),
    path('showSummary',views.showSummary,name='showSummary')
]
