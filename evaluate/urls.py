from django.urls import path
from . import views

urlpatterns = [
    path('evaluate', views.evaluate, name='evaluate'),
    path('saveAndShowSummary',views.saveAndShowSummary,name='saveAndShowSummary')
]
