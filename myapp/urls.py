from myapp import views
from django.urls import path,include


urlpatterns = [
    path('',views.home,name="home"),
    path('/searched',views.searched_location,name="searched_location"),
]