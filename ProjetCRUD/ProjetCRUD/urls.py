from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.fetch_data_from_api, name='fetch_data'),  # Assurez-vous que cette URL est correcte
    path('search/', views.search, name='search'),  # Définissez une URL pour la vue search
]
