## APP (Y-FI)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_document, name='upload'),
    path("<int:pk>/", views.document_detail, name="document_detail"),
]