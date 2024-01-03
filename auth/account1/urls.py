from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',login_attempt,name='login_attempt'),
    path('register/',register_attempt,name='register_attempt'),
    path('sucess/',sucess,name='sucess'),
    path('register/token/',token_send,name='token_send'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error")

    

         
]