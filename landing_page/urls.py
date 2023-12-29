from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/',views.about,name="about"),
    path('academics/',views.academics,name="academics"),
    path('academics/class1/',views.academics_class1,name="class1"),
    path('admission/',views.admission,name="admission"),
    path('register/',views.register,name="register"),
    path('signin/',views.signin,name="signin"),
    path('login/',views.login1,name="login"),
    path('logout/',views.logout1,name="logout"),
    path('profile/',views.profile,name="profile"),
    
    
]