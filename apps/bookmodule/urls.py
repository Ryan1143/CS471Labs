from django.urls import path
from . import views
path('<int:bookId>', views.viewbook)
urlpatterns = [
path('', views.index),
path('index2/<int:val1>/', views.index2)
    ]