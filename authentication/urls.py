from django.urls import include, path

from . import views

urlpatterns = [
    path('login/', include(views.Login_View)),
    
]