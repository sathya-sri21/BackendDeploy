from django.urls import path
from .views import *
urlpatterns=[
    path('shop',shop_page),
    path('signup',signup_page,name="signup"),
    path('login',login_page,name="login"),
    path('signup_handler',signup_handler)

]