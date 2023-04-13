from django.urls import path
from telenovelas import views 

urlpatterns = [
    path('',views.telenovelas,name='telenovelas')
]