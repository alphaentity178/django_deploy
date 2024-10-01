from django.urls import path
from deploy_app import views

app_name = 'deploy_app'

urlpatterns = [
    path('' , views.home , name='home'),
]
