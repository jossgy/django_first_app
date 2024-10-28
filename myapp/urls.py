
from django.urls import path
from .views import hello, about  # Asegúrate de usar el punto antes de 'views'

urlpatterns = [
    path('', hello, name='home'),  # Opcional: agrega un nombre para la vista
    path('about/', about, name='about'),  # Opcional: agrega un nombre para la vista
]
