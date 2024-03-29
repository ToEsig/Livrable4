import requests
from django.shortcuts import render
from .models import APIObject
from .forms import SearchForm
import requests
from django.shortcuts import render
from .models import APIObject
from .forms import SearchForm

def fetch_data_from_api(request):
    url = 'https://api.api-onepiece.com/v2/fruits/fr'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Traitez les données et enregistrez-les dans le modèle
        for item in data:
            api_object = APIObject(
                name=item['name'],  # Utilisez 'roman_name' au lieu de 'name'
                type=item['type'],
                description=item['description']
            )
            api_object.save()

        # Récupérer les objets depuis la base de données pour les afficher dans le template
        api_objects = APIObject.objects.all()
        # Affichez les fruits avec le formulaire de recherche dans le même template
        return render(request, 'Fruit.html', {'form': SearchForm(), 'api_objects': api_objects})
    else:
        return render(request, 'error.html', {'error_message': 'Failed to fetch data from API'})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Effectuer la recherche dans le modèle APIObject
            results = APIObject.objects.filter(name__icontains=query).distinct()  # Filtrer les résultats distincts
            # Renvoyer uniquement les résultats de recherche et le formulaire dans le même template
            return render(request, 'Fruit.html', {'form': form, 'results': results})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})

