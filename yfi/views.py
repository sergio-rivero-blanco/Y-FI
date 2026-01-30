from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Document, ExtractionResult
from .inference.service import process_document

def upload_document(request):
    if request.method == "POST":
        file = request.FILES["file"]
        doc_type = request.POST.get("doc_type", "AUTO")

        doc = Document.objects.create(
            file=file,
            doc_type=doc_type,
            status="PROCESSING",
        )

        try:
            result_json, provider = process_document(doc)

            ExtractionResult.objects.create(
                document=doc,
                result_json=result_json,
                provider=provider,
            )

            doc.status = "DONE"
            doc.save()
        except Exception:
            doc.status = "ERROR"
            doc.save()

        return redirect("document_detail", pk=doc.pk)

    return render(request, "yfi/upload.html")


def document_detail(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    result = ExtractionResult.objects.filter(document=doc).first()

    return render(request, "yfi/detail.html", {
        "document": doc,
        "result": result,
    })

def index(request):
    return HttpResponse("Y-FI index, will be implemented soon!")