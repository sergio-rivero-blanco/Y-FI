from .base import BaseInferenceProvider

class FakeInferenceProvider(BaseInferenceProvider):
    def infer(self, file_path: str, doc_type: str) -> dict:
        # Normalizamos auto a facturas para DEMO:
        if doc_type == "AUTO":
            doc_type = "FACTURA"
        if doc_type == "NOMINA":
           return {
                "doc_type": "nomina",
                "fields": {
                    "bruto": 1500.00,
                    "irpf": 200.00,
                    "seg_social": 100.00,
                    "neto": 1200.00,
                },
                "warnings": []
            }

        return {
            "doc_type": "factura",
            "fields": {
                "base": 100.00,
                "iva_pct": 21,
                "iva_cuota": 21.00,
                "total": 121.00,
            },
            "warnings": []
        }