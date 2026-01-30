from django.conf import settings
from .fake import FakeInferenceProvider

# Función que detecta en qué modo estamos, de momento los datos son fake, posteriormente
# se integrará la api donut para generar datos reales a partir de imágenes
def get_provider():
    if getattr(settings, "INFERENCE_PROVIDER", "fake") == "fake":
        return FakeInferenceProvider()
    return FakeInferenceProvider()


# Función que recoge el resultado de procesar la imágen y el tipo de provider que la realiza
def process_document(document):
    provider = get_provider()
    result = provider.infer(document.file.path, document.doc_type)
    return result, getattr(settings, "INFERENCE_PROVIDER", "fake")
