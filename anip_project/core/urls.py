from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # les vues qu’on va créer plus tard, ou placeholder
    path('ocr/', views.ocr_view, name='ocr_view'),
    path('compare/', views.compare_view, name='compare_view'),
    path('age/', views.age_view, name='age_view'),
]
