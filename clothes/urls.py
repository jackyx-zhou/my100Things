from django.urls import path
from . import views

urlpatterns = [
    path('api/clothes/', views.ClothingListCreate.as_view() ),
]
