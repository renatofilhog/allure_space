from django.urls import path
from usuarios.views import login, registrar

urlpatterns = [
      path('login',login, name='login'),
      path('registrar', registrar, name='registrar'),
]
