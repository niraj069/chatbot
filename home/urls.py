from django.urls import path
from home import views

urlpatterns = [
     path('', views.index , name='home'),
     path('nav', views.nav , name='nav'),
     path('std', views.std , name='std'),
]
