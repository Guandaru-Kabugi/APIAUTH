from django.urls import path
from .views import login,signup,test_token
urlpatterns = [
    path('login/',login),
    path('signup/',signup),
    path('test_token/',test_token),
]
