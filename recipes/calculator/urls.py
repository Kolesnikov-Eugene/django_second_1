from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('<recipe>/', views.recipe_view, name='recipe')
]