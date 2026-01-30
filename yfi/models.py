from django.db import models

# Create your models here.
class Document(models.Model):

    # CTEs de clase
    # Posibles tipos de documentos
    DOC_TYPES = [
        ("AUTO", "Automático"),
        ("FACTURA", "Factura"),
        ("NOMINA", "Nómina"),
    ]

    # Posibles estados de los documentos
    STATUS = [
        ("UPLOADED", "Uploaded"),
        ("PROCESSING", "Processing"),
        ("DONE", "Done"),
        ("ERROR", "Error"),
    ]

    file = models.FileField(upload_to="documents/")
    doc_type = models.CharField(max_length=10, choices=DOC_TYPES, default="AUTO")
    status = models.CharField(max_length=20, choices=STATUS, default="UPLOADED")

    def __str__(self):
        return f"Document {self.id} ({self.doc_type})"
    
class ExtractionResult(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    result_json = models.JSONField()
    provider = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for document {self.document.id}"