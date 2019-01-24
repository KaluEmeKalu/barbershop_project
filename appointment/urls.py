from django.urls import path
from appointment import views

app_name = "appointment"

urlpatterns = [
    path('', views.home_page, name="home_page"),
]
