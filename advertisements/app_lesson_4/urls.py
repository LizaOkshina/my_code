


from django.urls import path, include
from .views import index_1

urlpatterns = [
    path('', index_1)
]
