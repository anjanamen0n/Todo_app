#urls.py

from django.urls import path
from .views import LoginView, UserView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),

]



