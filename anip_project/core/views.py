from django.shortcuts import render
from django.shortcuts import render
import os
import cv2
import pytesseract
from .forms import OCRForm

# Create your views here.

def home(request):
    """
    Affiche la page d'accueil avec les boutons pour :
    - Extraire du texte (OCR)
    - Comparer des visages
    - Estimer l'âge
    """
    # On peut passer les liens vers les autres vues si elles existent déjà
    context = {
        # si déjà créées :
        'url_ocr': 'ocr_view',
        'url_compare': 'compare_view',
        'url_age': 'age_view',
    }
    return render(request, 'core/home.html', context)


def ocr_view(request):
    """
    Vue pour uploader une image et extraire le texte avec OCR.
    """
    result = None
    error = None

    if request.method == 'POST':
        form = OCRForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.cleaned_data['image']

            # Créer dossier media s'il n'existe pas
            media_folder = os.path.join('media', 'ocr_uploads')
            if not os.path.exists(media_folder):
                os.makedirs(media_folder)

            # Sauvegarder le fichier uploadé
            file_path = os.path.join(media_folder, uploaded.name)
            with open(file_path, 'wb+') as f:
                for chunk in uploaded.chunks():
                    f.write(chunk)

            # Lecture de l’image
            # On peut utiliser OpenCV pour lire
            img = cv2.imread(file_path)
            if img is None:
                error = "Impossible de lire l'image."
            else:
                # Conversion BGR → RGB (si besoin)
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Extraction de texte
                text = pytesseract.image_to_string(img_rgb)
                result = text
        else:
            error = "Formulaire invalide. Assure-toi d'avoir choisi une image."
    else:
        form = OCRForm()

    return render(request, 'core/ocr.html', {
        'form': form,
        'result': result,
        'error': error,
    })

def compare_view():
    pass

def age_view():
    pass