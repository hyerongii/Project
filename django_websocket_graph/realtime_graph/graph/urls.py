from django.urls import path
from .views import index

app_name = 'graph'
urlpatterns = [
    path('', index)
]